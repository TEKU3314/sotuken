from django.urls import path

from . import views


app_name = 'modify'
urlpatterns = [
    path('', views.ModifyView.as_view(), name="modify"),
    path('ajax-file-generate/', views.ajax_file_generate, name='ajax_file_generate'),
    path('file-upload/', views.file_upload, name='file_upload'),
    path('modify/', views.file_upload, name='file_upload')
]