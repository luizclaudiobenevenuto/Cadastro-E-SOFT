from django import forms

from .models import Cadastro
from .contants import UF_CHOICES


class DivErrorList(forms.utils.ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(
            ['<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])


class CadastroModelForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(CadastroModelForm, self).__init__(*args, **kwargs_new)

    class Meta:
        model = Cadastro
        fields = [
            "id",
            "cep",
            "cidade",
            "endereco",
            "numero",
            "complemento",
            "bairro",
            "uf",
            "descricao",
        ]
        widgets = {
            "cep": forms.TextInput(attrs={"class": "form-control"}, ),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.Select(choices=UF_CHOICES, attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_cep(self):
        cep = self.cleaned_data.get("cep")
        if len(cep) != 8:
            raise forms.ValidationError("CEP deve conter 9 caracteres")

        try:
            cep = int(cep)
        except ValueError:
            raise forms.ValidationError("CEP deve conter apenas números")
        return cep

    def clean_numero(self):
        numero = self.cleaned_data.get("numero")
        try:
            numero = int(numero)
        except ValueError:
            raise forms.ValidationError("Número deve conter apenas números")
        return numero

    def clean_uf(self):
        uf = self.cleaned_data.get("uf")
        if uf not in str(UF_CHOICES):
            raise forms.ValidationError("Estado inválido")
        return uf

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao")
        if len(descricao) > 500:
            raise forms.ValidationError("Descrição deve conter até 500 caracteres")
        return descricao



