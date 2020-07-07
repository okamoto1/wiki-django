from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki/", views.search, name="search"),
    path("create-entry", views.create_entry, name="create_entry"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("ramdom", views.randompick, name="random"),
]
