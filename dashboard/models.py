from django.db import models


# Create your models here.
TIPO = (
    ('Móvel', 'Móvel'),
    ('Eletrônico', 'Eletrônico'),
    ('Vestuário', 'Vestuário'),
    ('Beleza', 'Beleza'),
)

class Mercadoria(models.Model):
    nome = models.CharField(max_length=100, null=True)
    tipo = models.CharField(max_length=100, choices=TIPO, null=True)
    fabricante = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=100, null=True)
    quantidade = models.IntegerField(default=0)
    entradaQuantidade = models.IntegerField(default=0)
    saidaQuantidade = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Mercadoria'
    
    def __str__(self):
        return f'{self.nome}'
    
class Entrada(models.Model):
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(null=True)
    data = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'Entrada'
        
    def __str__(self):
        return f'{self.mercadoria}'