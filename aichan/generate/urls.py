from django.urls import path

from . import views


app_name = 'generate'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('generate/', views.GenetateView.as_view(), name="generate"),
    path('background/', views.BackGroundView.as_view(), name='background'),
    path('make_background/', views.make_background, name='make_background'),
    path('girl/', views.GirlView.as_view(), name='girl'),
    path('make_girl/', views.make_girl, name='make_girl'),
]