from django.db import models

# Create your models here.
class Distro(models.Model):
    # Campos de texto y contenido
    name = models.CharField(max_length=200)
    description = models.TextField()

    # registro activo o no
    active = models.BooleanField(default=True)

    # Metadatos automáticos
    created_at = models.DateTimeField(auto_now_add=True)

    # Gestión de archivos (requiere Pillow instalado)
    imagen = models.ImageField(upload_to='distros/', null=True, blank=True)

    # la distro rollin release o no
    rolling_release = models.BooleanField(default=False)

    # ultima vercion estable
    last_build_stable = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        # Programación defensiva: asegura que siempre devuelva un string
        return str(self.name)
