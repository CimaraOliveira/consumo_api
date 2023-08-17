from django.urls import path
from . import views

urlpatterns = [
   path('cadastro/', views.cadastro, name='cadastro'),
   path('requisicao_api', views.requisicao_api, name='requisicao_api'),
]