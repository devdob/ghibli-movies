from django.urls import path, include
from .views import MovieList
from django.views.generic import TemplateView

urlpatterns = [
    path('movies', MovieList.as_view())
]
