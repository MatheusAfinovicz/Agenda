from django.contrib import admin
from .models import Contato, Categoria


class ContadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao')
    list_display_links = ('id', 'nome', 'sobrenome', 'telefone', 'email')
    list_per_page = 10
    ordering = ('nome',)
    search_fields = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao')


admin.site.register(Categoria)
admin.site.register(Contato, ContadoAdmin)
