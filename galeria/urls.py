from django.urls import path
from galeria.views import index, imagem

app_name='galeria'

urlpatterns=[
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]