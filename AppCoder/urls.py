from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views




urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('leerRopa', views.ropa, name="Ropa"),
    path('ropa', views.agregarRopa, name="Agregar Prenda"),
    path('leerMaquillajes', views.maquillaje, name="Maquillaje"),
    path('maquillaje', views.agregarMaquillaje, name="Agregar maquillaje"),
    path('cartera_list', views.CarteraList.as_view(), name="Carteras"),
    path(r'(?P<pk>\d+)$', views.CarteraDetalle.as_view(), name="Detail"),
    path(r'^nuevo$', views.CarteraCreation.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.CarteraUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.CarteraDelete.as_view(), name="Delete"),
    #path('cartera', views.agregarCartera, name="Agregar Carteras"),
    path('eliminarCartera/<code_cartera>/', views.eliminarCartera, name="EliminarCartera"),
    path('editarCartera/<code_cartera>/', views.editarCartera, name="EditarCartera"),
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

]


