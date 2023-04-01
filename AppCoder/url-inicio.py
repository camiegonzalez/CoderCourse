from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
]


