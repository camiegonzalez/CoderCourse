from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views




urlpatterns = [
    path('pages', views.BlogList.as_view(), name="Pages"),
    path(r'(?P<pk>\d+)$', views.BlogDetalle.as_view(), name="PagesDetail"),
    path(r'^borrar/(?P<pk>\d+)$', views.BlogDelete.as_view(), name="PagesDelete"),
    path(r'^nuevo$', views.BlogCreation.as_view(), name="PagesNew"),
    path(r'^editar/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name="PagesEdit"),
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('message_list', views.messages, name="Messages"), #esta era nuestra primer view
    path('about', views.about, name="About"), #esta era nuestra primer view
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('verPerfil', views.verPerfil, name="Perfil"), 
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),
]


