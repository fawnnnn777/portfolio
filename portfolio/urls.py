from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login_view"),
    path('logout', views.logout_view, name="logout_view"),
    path('create', views.create, name="create"),
    path('register', views.register, name="register"),
    path('create', views.create, name="create"),
    path('myporto', views.myporto, name="myporto")
    ]
