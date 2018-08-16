from django.urls import path
from .views import MovieList
from django.views.generic.base import RedirectView

urlpatterns = [
    path('movies', MovieList.as_view(), name='movies-list'),
    path('', RedirectView.as_view(url='movies', permanent=False), name='index')
]
