from django.forms import ModelForm
from .models import Distros

class TaskForm(ModelForm):
  class Meta:
    model = Distros
    fields = '__all__'
