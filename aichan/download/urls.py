from django.urls import path

from . import views


app_name = 'download'
urlpatterns = [
    path('<slug:file>/', views.download,name='download'),
]