from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'modulo/indexadmin.html')
    else:
        return render(request, 'modulo/index.html')

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
