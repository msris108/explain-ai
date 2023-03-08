from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.home, name=""),
    path("home", views.home, name="home"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("free", views.free, name="free"),
    path("pro", views.pro, name="pro"),
]