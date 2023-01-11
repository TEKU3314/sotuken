from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from datetime import datetime

from .forms import ModifyForm
from download.models import Image

import json
import cv2

class ModifyView(CreateView):
    template_name = "fileupload.html"
    form_class = ModifyForm

def file_upload(request):
    if request.method == "POST":
        form = ModifyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES['image']
            post.save()
            print(post.pk)
            context = {'ID':post.pk}
            return render(request, 'modify.html', context)

def ajax_file_generate(request):

    dic = QueryDict(request.body, encoding='utf-8')

    width = dic.get('width')
    height = dic.get('height')
    id = dic.get('id')

    print('------------------------------------------------------')
    print('幅')
    print(width)
    print('高さ')
    print(height)
    print('平滑化')
    print()
    print('id')
    print(id)
    print('------------------------------------------------------')

    #画像の読み取り
    img = Image.objects.get(id=id) 
    filename = "./media/" + str(img.image)
    img = cv2.imread(filename)

    #### 画像のリサイズ　#####

    #画像のサイズ変更
    size = (int(width),int(height))
    img = cv2.resize(img,size)

    #### 画像のリサイズ　#####
    

    #####   画像のノイズ除去・平滑化処理  #####

    #平滑化フィルタによるノイズ除去　｜　cv2.blur
    img = cv2.blur(img,(9,9))

    #メディアンフィルタによるノイズ除去　|　cv2.medianBlur
    img = cv2.medianBlur(img,1)

    #ガウシアンフィルタによるノイズ除去　｜　cv2.GaussianBlur
    img = cv2.GaussianBlur(img,(9,9),2)

    #バイラテラルフィルタによるノイズ除去　｜　cv2.bilateralFilter
    img = cv2.bilaateralFilter(img,100,120,10)

    #####   画像のノイズ除去・平滑化処理  #####


    #画像の保存
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    pngno = date
    filename = "./media/" + date + ".png" 
    cv2.imwrite(filename,img) 

    d = {
        'result': pngno,
    }

    return JsonResponse(d)



