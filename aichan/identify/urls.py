from django.urls import path

from . import views


app_name = 'identify'
urlpatterns = [
    path('identify/', views.IdentifyView.as_view(), name="identify"),
]