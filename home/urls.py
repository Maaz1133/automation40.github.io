from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.home_new, name='home'),
    path("newarti", views.Arti, name='Arti'), 
    path("chatgpt", views.chatgpt, name='Arti1'), 
    path("logedin", views.loginmyy, name='loginmyy'), 
    path("createAccount", views.signup, name='signup'), 
    path("logout", views.logoutPage, name='logout'), 
    path("Automation", views.automation, name='automation'), 
    path('search', views.search, name='search'),
    path('add/', views.create_blog_post, name='add_post'),
    path('post/<str:URL>', views.edit_blog_post, name='post_detail'),

]