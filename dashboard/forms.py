from django import forms
from .models import Mercadoria

class MercadoriaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['nome', 'tipo', 'fabricante', 'descricao',]
        
        
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['entradaQuantidade',]       

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['saidaQuantidade',]       
