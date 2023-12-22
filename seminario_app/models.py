from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )

    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField()
    
    def obtener_nombre_institucion(self):
        return self.id_institucion.nombre