from django.urls import path, include
from . import views

# template_url
app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.login_required, name='logout'),
    path('login/', views.user_login, name='login')

]
