from django.db import models

from django.db.models import signals
from django.forms import ValidationError
from django.template.defaultfilters import slugify

from .contants import UF_CHOICES

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cadastro(Base):
    cep = models.CharField('CEP', max_length=9)
    cidade = models.CharField('Cidade', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Número', max_length=8)
    complemento = models.CharField('Complemento', max_length=20)
    bairro = models.CharField('Bairro', max_length=50)
    uf = models.CharField('Estado', max_length=2, choices=UF_CHOICES)
    descricao = models.TextField('Descrição')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.cep


def cadastro_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.cep)

signals.pre_save.connect(cadastro_pre_save, sender=Cadastro)
