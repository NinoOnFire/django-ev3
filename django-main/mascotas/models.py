from django.db import models
from django.contrib.auth.models import User

class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.nombre} - {self.raza}"

    class Meta:
        db_table = 'mascota'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'


class Cliente(models.Model):
    id = models.AutoField(primary_key=True) 
    Run_Cliente = models.CharField(max_length=10)  
    Nombre_Cliente = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=254)  
    Telefono = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.Nombre_Cliente} {self.Apellido}"


class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    Id = models.AutoField(primary_key=True)
    Run_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='solicitudes')
    Nombre_Mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE, related_name='solicitudes')
    Detalle = models.TextField()
    Fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Solicitud {self.Id} - {self.Run_Cliente.Nombre_Cliente} ({self.get_estado_display()})"


