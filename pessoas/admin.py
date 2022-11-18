from django.contrib import admin
from setuptools import sic
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome_teceita',)
    list_per_page = 2


admin.site.register(Pessoa, ListandoPessoas)

