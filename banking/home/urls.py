from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('login', views.login,name = 'login'),
    path('register', views.register,name = 'register'),
    path('logout',views.logout,name ='logout'),
    path('newpage',views.newpage,name = 'newpage'),
    path('form',views.form,name = 'form'),
    path('ajax/load-branch-details/', views.load_branch_details, name='ajax-load-branch'),




]