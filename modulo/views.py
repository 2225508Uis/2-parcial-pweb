from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Distro
from .forms import DistroForm


# Create your views here.
def index_view(request, ord):
    """wiki"""
    if ord == 1:
        ordenp ='created_at'
        orden = 'Ascendente'

    else:
        ordenp = '-created_at'
        orden = 'Descendente'
    if not request.user.is_authenticated:
        distros = Distro.objects.filter(active=True).order_by(ordenp)
    else:
        distros = Distro.objects.all().order_by(ordenp)


    context = {
        'distros': distros,
        'emoji_done': '✅',
        'emoji_pending': '⛔',
        'orden': orden,

    }

    if request.user.is_authenticated:
        return render(request, 'modulo/indexadmin.html', context)
    else:
        return render(request, 'modulo/index.html', context)

def login_view(request):
    """login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index', ord=0)
        else:
            return render(request, 'modulo/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'modulo/login.html')

def logout_view(request):
    logout(request)
    return redirect('index', ord=0)

def descripcion_view(request, id):
    """descripcion de la distro"""
    distro = Distro.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, 'modulo/descripcion.html', {'distro': distro, 'admin': True,'emoji_done': '✅', 'emoji_pending': '⛔',})
    return render(request, 'modulo/descripcion.html', {'distro': distro, 'admin': False})

@login_required
def create(request):
    """crear distro"""
    if request.method == 'POST':
        form = DistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = DistroForm()
    return render(request, 'modulo/create.html', {'form': form, 'creando': True})

@login_required
def update(request, id):
    """actualizar distro"""
    distro = Distro.objects.get(id=id)
    form = DistroForm(request.POST or None, request.FILES or None, instance=distro)
    if form.is_valid():
        form.save()
        return redirect('index', ord=0)
    return render(request, 'modulo/create.html', {'form': form, 'creando': False})
@login_required
def delete(request, id):
    """eliminar distro"""
    distro = Distro.objects.get(id=id)
    distro.delete()
    return redirect('index', ord=0)
