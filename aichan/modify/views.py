from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from datetime import datetime

from .forms import ModifyForm
from download.models import Image

import json
import cv2
import numpy as np

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
    print('---------')

def ajax_file_generate(request):

    dic = QueryDict(request.body, encoding='utf-8')

    width = dic.get('width')
    height = dic.get('height')
    filter = dic.get('filter')
    mono = dic.get('mono')
    gamma = dic.get('gamma')
    id = dic.get('id')

    print('------------------------------------------------------')
    print('幅')
    print(width)
    print('高さ')
    print(height)
    print('ガンマ')
    print(gamma)
    print('平滑化')
    print(filter)
    print('モノクロ')
    print(mono)
    print('id')
    print(id)
    print('------------------------------------------------------')

    #画像の読み取り
    img = Image.objects.get(id=id) 
    filename = "./media/" + str(img.image)
    img = cv2.imread(filename)

    #### 画像のリサイズ　#####

    #画像のサイズ変更
    if height and width:
        size = (int(width),int(height))
        img = cv2.resize(img,size)

    #####   画像のノイズ除去・平滑化処理  #####
    if filter == "1":
        #平滑化フィルタによるノイズ除去　｜　cv2.blur
        img = cv2.blur(img,(9,9))
        print('aaaaaaaa')
    elif filter == "2":
        #メディアンフィルタによるノイズ除去　|　cv2.medianBlur
        img = cv2.medianBlur(img,1)
        print('bbbbbbbb')
    elif filter == "3":
        #ガウシアンフィルタによるノイズ除去　｜　cv2.GaussianBlur
        img = cv2.GaussianBlur(img,(9,9),2)
        print('cccccccc')
    elif filter == "4":
        #バイラテラルフィルタによるノイズ除去　｜　cv2.bilateralFilter
        img = cv2.bilateralFilter(img,100,120,10)
        print('dddddddd')
    else:
        print()


    #OpenCVによる画像の2値化処理・モノクロ変換
    # グレースケールに変換
    if (mono == 'true'):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # モノクロ化
        threshold  = 100
        ret,th_img = cv2.threshold(img,                # 画像データ
                                    100,                # 閾値
                                    255,                # 閾値を超えた画素に割り当てる値
                                    cv2.THRESH_BINARY   # 閾値処理方法
                                )

    #OpenCVによるガンマ補正
    # ガンマ変換用の数値準備 
    if (gamma):
        gamma = float(gamma)
        img2gamma = np.zeros((256,1),dtype=np.uint8)  # ガンマ変換初期値

        # 公式適用
        for i in range(256):
            img2gamma[i][0] = 255 * (float(i)/255) ** (1.0 /gamma)

        # 読込画像をガンマ変換
        img = cv2.LUT(img,img2gamma)

    #画像の保存
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    pngno = date
    filename = "./media/" + date + ".png" 
    cv2.imwrite(filename,img) 

    d = {
        'result': pngno,
    }

    return JsonResponse(d)
    