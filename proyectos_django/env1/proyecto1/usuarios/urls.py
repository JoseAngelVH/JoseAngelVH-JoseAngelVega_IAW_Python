from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista_usuarios, name='lista'),
    path('excel/', views.exportar_excel, name='excel'),
]
