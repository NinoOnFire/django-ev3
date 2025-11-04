from django import forms
from .models import Cliente, Solicitud, Mascotas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Run_Cliente', 'Nombre_Cliente', 'Apellido', 'Correo', 'Telefono']
        widgets = {
            'Run_Cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUN del cliente'}),
            'Nombre_Cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellido'}),
            'Correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono'}),
        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        # Los únicos campos que el usuario debe llenar
        fields = ['Nombre_Mascota', 'Detalle']
        widgets = {
            'Nombre_Mascota': forms.Select(attrs={'class': 'form-select'}),
            'Detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe por qué quieres adoptar esta mascota...'}),
        }

# Este formulario es para que un ADMINISTRADOR edite/gestione una solicitud.
class SolicitudAdminForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['Run_Cliente', 'Nombre_Mascota', 'Detalle', 'estado']
        widgets = {
            # Solo definimos las clases de CSS aquí
            'Run_Cliente': forms.Select(attrs={'class': 'form-select'}),
            'Nombre_Mascota': forms.Select(attrs={'class': 'form-select'}),
            'Detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        # Primero, se ejecuta el __init__ normal del formulario
        super().__init__(*args, **kwargs)
        
        # self.instance es el objeto Solicitud que se está editando.
        # Si self.instance.pk existe, significa que estamos EDITANDO 
        # una solicitud existente (no creando una nueva).
        if self.instance and self.instance.pk:
            
            # Esta es la forma correcta de deshabilitar los campos:
            # Django renderizará el widget como 'disabled' Y 
            # sabrá que no debe esperar estos datos en el POST.
            self.fields['Run_Cliente'].disabled = True
            self.fields['Nombre_Mascota'].disabled = True
            self.fields['Detalle'].disabled = True
            
            # El campo 'estado' permanece editable por defecto.

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = ['nombre', 'raza', 'descripcion', 'foto']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pug, Gato Siamés'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        