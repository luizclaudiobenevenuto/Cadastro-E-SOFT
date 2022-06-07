from django.contrib import admin

from .models import Cadastro

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('cep', 'cidade', 'endereco', 'numero', 'complemento', 'bairro', 'uf', 'descricao', 'slug',
                    'criado', 'ativo', 'modificado')
