from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PerssoaAdmin(admin.ModelAdmin):
    model = Pessoa
    list_display = ['nome']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome',]