from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegistroForm, CambiarUsuarioForm
from .models import Usuario
# Register your models here.


class UsuarioAdmin(UserAdmin):
    add_form = RegistroForm
    form = CambiarUsuarioForm
    model = Usuario
    list_display = ['email', 'username',]

admin.site.register(Usuario, UsuarioAdmin)