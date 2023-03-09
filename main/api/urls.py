from django.urls import path 
from . import views

urlpatterns = [
    path("", views.getApiRoutes),
    path("explain/<str:query>/<str:model>/<str:level>", views.getPrompt),
    path("linkedin/<str:query>", views.getLinkedInPost),
    path("movie/<str:query>", views.getMovieSummary),
]