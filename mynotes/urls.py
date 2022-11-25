from django.contrib import admin
from django.urls import path
from.views import index
from .import views
import django.contrib.auth.views as auth_views

app_name='mynotes'

urlpatterns=[
path('',index,name='index'),
path('home/',views.home,name='home'),
path('add-note/',views.add_note,name='add_note'),
path('register/',views.register,name='register'),
path('login/',views.userlogin,name='login'),
path('account/',views.account_settings,name='account_settings'),

path('logout/',auth_views.LogoutView.as_view(template_name='mynotes/logout.html'),name='logout'),
path('error/',views.reg_error,name='reg_error'),
path('update/<int:pk>/',views.update,name='update'),
path('delete/<int:pk>/',views.delete,name='delete'),
path('search/',views.search_note,name='search'),

]