from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('user',views.user,name='user'),
    path('adminpage',views.admin,name='admin'),
    path('apply',views.apply,name='apply'),
    path('signupadmin',views.signupadmin,name='signupadmin'),
    path('available',views.available,name='available'),
]