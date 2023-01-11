from django.urls import path

from . import views


app_name = 'identify'
urlpatterns = [
    path('', views.IdentifyView.as_view(), name="identify"),
]