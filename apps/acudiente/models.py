from django.db import models

# Create your models here.

class persona(models.Model):

    GRUPO = [
        ('RO', 'O+'),
        ('RA', 'A+'),
        ('RA2', 'A-'),
        ('RB', 'B+'),
        ('RB2', 'B-'),
        ('RAB', 'AB+'),
        ('RAB2', 'AB-'),
        ('RO2', 'O-'),
    ]

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    telefono = models.CharField(max_length=12)
    edad = models.IntegerField()
    email = models.EmailField()
    direccion = models.TextField()
    grupo_rh = models.CharField(max_length=10, choices=GRUPO)

    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellidos
