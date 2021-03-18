from django.contrib import admin
from .models import produto

@admin.register(produto)
class produtoAdm(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')