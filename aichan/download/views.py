from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render

from .models import Image

import requests


def download(request,file):
      context = {'file':file}
      print(file)

      return render(request,'download.html',context)





