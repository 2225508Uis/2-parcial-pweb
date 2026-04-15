from django.forms import ModelForm
from .models import Distro

class TaskForm(ModelForm):
  class Meta:
    model = Distro
    fields = '__all__'
