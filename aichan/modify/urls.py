from django.urls import path

from . import views


app_name = 'modify'
urlpatterns = [
    path('modify/', views.ModifyView.as_view(), name="modify"),
]