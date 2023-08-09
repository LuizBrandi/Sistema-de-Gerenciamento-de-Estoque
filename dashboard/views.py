from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Mercadoria
from .forms import MercadoriaForm, EntradaForm, SaidaForm

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def mercadoria(request):
    items = Mercadoria.objects.all()
    # items = Mercadoria.objects.raw('SELECT * FROM dashboard_mercadoria')
    
    if request.method == 'POST':
        form = MercadoriaForm(request.POST)
        if form.is_valid():
            form.save()
            nomeMercadoria = form.cleaned_data.get('nome')
            messages.add_message(request, messages.ERROR, f'Mercadoria({nomeMercadoria}) adicionada', extra_tags='green')
            # messages.success(request, f'Mercadoria({nomeMercadoria}) adicionada')
            return redirect('dashboard-mercadorias')
    else:
        form = MercadoriaForm()
        
        
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/mercadorias.html', context)

def mercadoria_delete(request, pk):
    item = Mercadoria.objects.get(id = pk)
    
    if request.method == 'POST':
        item.delete()
        nomeMercadoria = item.nome
        messages.add_message(request, messages.ERROR, f'Mercadoria({nomeMercadoria}) removida', extra_tags='red')
        return redirect('dashboard-mercadorias')
    
    return render(request, 'dashboard/mercadorias_delete.html') 

def mercadoria_update(request, pk):
    item = Mercadoria.objects.get(id = pk)
    if  request.method == 'POST':
        form = MercadoriaForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            nomeMercadoria = item.nome
            messages.add_message(request, messages.ERROR, f'Mercadoria({nomeMercadoria}) editada', extra_tags='blue')
            return redirect('dashboard-mercadorias')
    else:
        form = MercadoriaForm(instance = item)
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/mercadorias_update.html', context) 


def movimentacao(request):
    items = Mercadoria.objects.all()
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-movimentacao')
    else:
        form = EntradaForm()
        
        
    context = {
        'items': items,
        'form': form,
    }
    
    return render(request, 'dashboard/movimentacao.html', context)


def entrada_update(request, pk):
    item = Mercadoria.objects.get(id = pk)
    if  request.method == 'POST':
        form = EntradaForm(request.POST, instance = item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantidade += instance.entradaQuantidade
            instance.save()
            nomeMercadoria = item.nome
            quantidadeMercadoria = item.entradaQuantidade
            messages.add_message(request, messages.ERROR, f'Nova entrada({quantidadeMercadoria} {nomeMercadoria})', extra_tags='blue')
            return redirect('dashboard-movimentacao')
    else:
        form = EntradaForm(instance = item)
        
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'dashboard/registrar_entrada.html', context) 


def saida_update(request, pk):
    item = Mercadoria.objects.get(id = pk)
    if  request.method == 'POST':
        form = SaidaForm(request.POST, instance = item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantidade -= instance.saidaQuantidade
            instance.save()
            nomeMercadoria = item.nome
            quantidadeMercadoria = item.saidaQuantidade
            messages.add_message(request, messages.ERROR, f'Nova saida({quantidadeMercadoria} {nomeMercadoria})', extra_tags='red')
            return redirect('dashboard-movimentacao')
    else:
        form = EntradaForm(instance = item)
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/registrar_saida.html', context) 


def relatorio(request):
    mercadorias = Mercadoria.objects.all()
    
    context = {
        'mercadorias': mercadorias,
    }
    return render(request, 'dashboard/relatorio.html', context)