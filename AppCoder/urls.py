from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views




urlpatterns = [
    path('pages', views.BlogList.as_view(), name="Pages"),
    path('pages/<pk>/detail', views.BlogDetalle.as_view(), name="PagesDetail"),
    path('pages/<pk>/update', views.BlogUpdate.as_view(), name="PagesEdit"),
    path('pages/<pk>/delete', views.BlogDelete.as_view(), name="PagesDelete"),
    path('pages/create', views.BlogCreation.as_view(), name="PagesNew"),
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('message_list', views.messages, name="Messages"), #esta era nuestra primer view
    path('about', views.about, name="About"), #esta era nuestra primer view
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('user/creation', views.UserCreation.as_view(), name = 'Register'),
    path('user/<pk>/detail', views.UserDetail.as_view(), name="Perfil"), 
    path('user/<pk>/update', views.UserUpdateView.as_view(), name="EditarPerfil"), 
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),
]


