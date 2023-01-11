from django.urls import path

from . import views


app_name = 'modify'
urlpatterns = [
    path('', views.ModifyView.as_view(), name="modify"),
    path('ajax-file-send/', views.ajax_file_send, name='ajax_file_send')
]