# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Definindo a classe CustomUserAdmin para personalizar o comportamento do admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Campos a serem exibidos na lista de usuários
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    
    # Campos que podem ser filtrados na lista de usuários
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # Campos para pesquisa
    search_fields = ('email', 'username', 'first_name', 'last_name')
    
    # Campos que serão editáveis diretamente na lista de usuários
    ordering = ('email',)
    
    # Campos que aparecem ao editar um usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Campos que aparecem na criação de um usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff'),
        }),
    )

# Registrando o modelo CustomUser com a classe CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
