from django.contrib import admin
from .models import Contato, Categoria


class ContadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome', 'email')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email', 'data_criacao')
    list_editable = ('telefone', 'mostrar',)


admin.site.register(Categoria)
admin.site.register(Contato, ContadoAdmin)
