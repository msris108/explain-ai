from django.urls import path 
from . import views

urlpatterns = [
    path("", views.getApiRoutes),
    path("explain/<str:query>/<str:model>/<str:level>", views.getPrompt),
]