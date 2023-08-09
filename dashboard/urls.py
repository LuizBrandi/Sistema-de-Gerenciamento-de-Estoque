from django.urls import path
#o '.' indica a pasta atual
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('mercadorias/', views.mercadoria, name='dashboard-mercadorias'),
    path('mercadorias/delete/<int:pk>/', views.mercadoria_delete, name='dashboard-mercadoria-delete'),
    path('mercadorias/update/<int:pk>/', views.mercadoria_update, name='dashboard-mercadoria-update'),
    path('movimentacao/', views.movimentacao, name='dashboard-movimentacao'),
    path('movimentacao/entrada/<int:pk>/', views.entrada_update, name='dashboard-entrada-update'),
    path('movimentacao/saida/<int:pk>/', views.saida_update, name='dashboard-saida-update'),
    path('relatorio/', views.relatorio, name='dashboard-relatorio'),
]