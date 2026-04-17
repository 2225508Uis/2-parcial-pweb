"""Formulario para crear y editar distros"""
from django.forms import ModelForm
from .models import Distro

class TaskForm(ModelForm):
    """Formulario para crear y editar distros"""
    class Meta:
        """Definición de metadatos para el formulario"""
        model = Distro
        fields = '__all__'
