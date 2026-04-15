from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Distro
from .forms import TaskForm


# Create your views here.
def index(request):
    distros = Distro.objects.all().order_by('-created_at')
    context = {
        'distros': distros,
        'emoji_done': '✅',
        'emoji_pending': '⛔'
    }

    if request.user.is_authenticated:
        return render(request, 'modulo/indexadmin.html', context)
    else:
        return render(request, 'modulo/index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'modulo/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'modulo/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')
