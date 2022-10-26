from django.urls import path

from . import views


app_name = 'generate'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('generate/', views.GenetateView.as_view(), name="generate"),
]