from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar, name='cadastro'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
]
