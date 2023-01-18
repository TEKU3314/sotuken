from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponse, QueryDict
from diffusers import StableDiffusionPipeline
from datetime import datetime
from PIL import Image

import numpy as np

import torch
from torch import autocast

import cv2
import json
import base64
import requests
import logging
import time
import os

from .models import Word
from .models import Type
from download.models import Image

logger = logging.getLogger(__name__)

def make_background(request):
    time.sleep(1)
    
    dic = QueryDict(request.body, encoding='utf-8')
    style = dic.get('style')
    nature = dic.get('nature')
    building = dic.get('building')

    print('------------------------------------------------------')
    print('自然')
    print(nature)
    print('〇〇風')
    print(style)
    print('建物')
    print(building)
    print('------------------------------------------------------')

    #呪文生成
    zyumon = ''
    if style:
        zyumon  = zyumon + style + ' '

    if nature:
        zyumon = zyumon + nature + ' '

    if building:
        zyumon = zyumon + building + ' '


    #HuggingFaceのトークン
    HF_TOKEN = "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"

    #StableDiffusionパイプライン設定
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=HF_TOKEN)
    #pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion", torch_dtype=torch.float32)
    #pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion", use_auth_token=HF_TOKEN)
    pipe.to("cpu")

    prompt = zyumon
    image = pipe(prompt, height=512, width=768)["sample"][0]


    date = datetime.now().strftime("%Y%m%d_%H%M%S") #現在の日時を取得
    pngno = date
    filename = "./media/" + date + ".png" #ファイル名を生成した日時にする
    image.save(filename)

    d = {
        'result': pngno,
    }

    return JsonResponse(d)

def make_girl(request):
    time.sleep(1)
    
    #チェックボックスで選択したものを受け取る（name受け取り）
    dic = QueryDict(request.body, encoding='utf-8')

    style = dic.get('style')
    nature = dic.get('nature')
    building = dic.get('building')

    print('------------------------------------------------------')
    print('自然')
    print(nature)
    print('〇〇風')
    print(style)
    print('動物')
    print(animal)
    print('海')
    print(sea)
    print('建物')
    print(building)
    print('------------------------------------------------------')

    #呪文生成
    zyumon = ''
    if style:
        zyumon  = zyumon + style + ' '

    if nature:
        zyumon = zyumon + nature + ' '

    if building:
        zyumon = zyumon + building + ' '

    if sea:
        zyumon = zyumon + sea + ' '

    if animal:
        zyumon = zyumon + animal + ' '


    #HuggingFaceのトークン
    HF_TOKEN = "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"

    #StableDiffusionパイプライン設定
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=HF_TOKEN)
    #pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion", torch_dtype=torch.float32)
    print('--------------------------------------------------------------------------')
    #pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion", use_auth_token=HF_TOKEN)
    #使用するデバイスを設定
    #pipe.to("cuda")
    pipe.to("cpu")
    print('--------------------------------------------------------------------------')

    # 生成したい画像を指示
    # prompt = "anime,kuudere,solo,kawaii,8k,lips,beautiful blue eyes,lips,Uniform,highschool,japanese anime,highres,portrait"
    prompt = zyumon
    print('--------------------------------------------------------------------------')

    #画像生成
    print('--------------------------------------------------------------------------')
    image = pipe(prompt, height=512, width=768)["sample"][0]
    print('--------------------------------------------------------------------------')


    #生成した画像をファイル出力
    date = datetime.now().strftime("%Y%m%d_%H%M%S") #現在の日時を取得
    pngno = date
    filename = "./media/" + date + ".png" #ファイル名を生成した日時にする
    print('--------------------------------------------------------------------------')
    image.save(filename)

    print(filename)

    #生成した画像を取り出す
    #img = Image.open(filename)
    print('--------------------------------------------------------------------------')
    print('sssssss')
    #img = cv2.imread(filename)
    print('dddddddd')
    #print(img)



    #データベースに画像を保存
    print('qqqqqqqqqqq')
    
    #生成した画像を消す
    #os.remove(filename)

    #dのresultに生成した画像のファイル名を格納する
    d = {
        'result': pngno,
    }

    print('ddddddddddddd')
    return JsonResponse(d)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.TemplateView):
    template_name = "generate.html"

class BackGroundView(generic.ListView):
    model = BackGroundWord
    template_name = "background.html"

    def get_queryset(self):
        result = Word.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_background w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result

class GirlView(generic.ListView):
    model = GirlWord
    template_name = "girl.html"

    def get_queryset(self):
        result = Word.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_girl w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result

