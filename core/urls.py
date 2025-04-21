from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index , name='coreindex'),
    path('contact/', views.contact , name = 'contact'),
    path('signup/', views.signup , name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html' , authentication_form = LoginForm) , name = 'login'),

]