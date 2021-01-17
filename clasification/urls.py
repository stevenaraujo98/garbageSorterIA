from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("procesar/", views.sorter, name="sorter"),
]