from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from mascotas.models import Mascotas
from .froms import ClienteForm, SolicitudForm, MascotaForm, SolicitudAdminForm, Cliente
from .models import Solicitud

# --- Vistas de Administración de Solicitudes ---

# Función para comprobar si el usuario es un administrador (staff)
def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin) # Protege la vista solo para admins
def gestionar_solicitud(request, pk):
    """
    Vista para editar (gestionar) el estado de una solicitud.
    """
    solicitud = get_object_or_404(Solicitud, pk=pk)
    
    if request.method == 'POST':
        # Si el formulario se envía, se procesa con los datos nuevos
        form = SolicitudAdminForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            # Redirige a la lista de solicitudes (asumo que tienes una)
            return redirect('lista_solicitudes') 
    else:
        # Si es GET, solo muestra el formulario con los datos actuales
        form = SolicitudAdminForm(instance=solicitud)
        
    return render(request, 'mascotas/gestionar_solicitud.html', {
        'form': form
    })

@login_required
@user_passes_test(es_admin) # Protege la vista solo para admins
def eliminar_solicitud(request, pk):
    """
    Vista para confirmar y eliminar una solicitud.
    """
    solicitud = get_object_or_404(Solicitud, pk=pk)
    
    if request.method == 'POST':
        # Si el admin confirma (envía el formulario), se borra
        solicitud.delete()
        return redirect('lista_solicitudes')
        
    # Si es GET, solo muestra la página de confirmación
    return render(request, 'mascotas/confirmar_eliminar_solicitud.html', {
        'solicitud': solicitud
    })

# (Necesitarás también una vista para la lista, si aún no la tienes)
@login_required
@user_passes_test(es_admin)
def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('Fecha') # Muestra todas
    return render(request, 'mascotas/lista_solicitudes.html', {'solicitudes': solicitudes})



# Create your views here.

def galeria(request):
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas }
    return render(request, 'galeria.html', data)

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def crear_cliente_y_solicitud(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        solicitud_form = SolicitudForm(request.POST)

        if cliente_form.is_valid() and solicitud_form.is_valid():
            # Guardamos el cliente
            cliente = cliente_form.save()

            # Creamos la solicitud asociada a ese cliente
            solicitud = solicitud_form.save(commit=False)
            solicitud.Run_Cliente = cliente
            solicitud.save()

            return redirect('solicitudes')  # Cambia por la URL que corresponda

    else:
        cliente_form = ClienteForm()
        solicitud_form = SolicitudForm()

    context = {
        'cliente_form': cliente_form,
        'solicitud_form': solicitud_form
    }
    return render(request, 'solicitud.html', context)

def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-Fecha')
    context = {'solicitudes': solicitudes}
    return render(request, 'solicitudes.html', context)



# READ: Vista para listar todas las mascotas
def lista_mascotas(request):
    mascotas = Mascotas.objects.all()
    return render(request, 'galeria', {'mascotas': mascotas})

# CREATE: Vista para crear una nueva mascota
def crear_mascota(request):
    if request.method == 'POST':
        # Importante: pasamos request.FILES para manejar la subida de la imagen
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria') # Redirige a la lista después de crear
    else:
        form = MascotaForm()
    return render(request, 'form_mascota.html', {'form': form})

# UPDATE: Vista para editar una mascota existente
def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascotas, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'form_mascota.html', {'form': form})

# DELETE: Vista para eliminar una mascota
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascotas, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('galeria')
    return render(request, 'confirmar_eliminar.html', {'mascota': mascota})




@login_required # Opcional: protege la lista de clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# 2. CREATE (Crear)
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form, 'accion': 'Crear'})

# 3. UPDATE (Actualizar)
@login_required
def editar_cliente(request, pk):
    # Usamos 'pk' porque tu modelo usa 'id' como AutoField(primary_key=True)
    cliente = get_object_or_404(Cliente, pk=pk) 
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form_cliente.html', {'form': form, 'accion': 'Actualizar'})

# 4. DELETE (Eliminar)
@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    
    # Si es GET, muestra la confirmación
    return render(request, 'clientes/confirmar_eliminar_cliente.html', {'cliente': cliente})