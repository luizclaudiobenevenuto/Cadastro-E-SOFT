from django.urls import path

from .views import index, cadastro, update


urlpatterns = [
    path('', index, name='index'),
    path('cadastros/', cadastro, name='cadastros'),
    path('cadastros/<int:id>/', update, name='atualizacao'),
]

