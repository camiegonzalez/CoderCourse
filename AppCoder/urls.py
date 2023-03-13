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
    path('leerCarteras', views.carteras, name="Carteras"),
    path('cartera', views.agregarCartera, name="Agregar Carteras"),
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

]


