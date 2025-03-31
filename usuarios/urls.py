from django.urls import path
from .views import login_view, bienvenida_view

urlpatterns = [
    path('', login_view, name='login'),
    path('bienvenida/', bienvenida_view, name='bienvenida'),
]
