from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("<int:pk>/comments/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
]
