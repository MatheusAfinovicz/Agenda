from django.contrib import admin
from .models import Contato, Categoria


class ContadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao')
    list_display_links = ('id', 'nome', 'sobrenome', 'email')
    list_filter = ('nome', 'sobrenome', 'data_criacao')
    list_per_page = 10
    ordering = ('id',)


admin.site.register(Categoria)
admin.site.register(Contato, ContadoAdmin)
