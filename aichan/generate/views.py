from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponse, QueryDict
from diffusers import StableDiffusionPipeline, DDIMScheduler
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

from .models import BackGroundWord
from .models import GirlWord
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


    HF_TOKEN = "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"

    pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion",use_auth_token=HF_TOKEN,torch_dtype=torch.float16,)
    #pipe = StableDiffusionPipeline.from_pretrained("hakurei/waifu-diffusion", )

    pipe.to("cuda")



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

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.TemplateView):
    template_name = "generate.html"

class BackGroundView(generic.ListView):
    model = BackGroundWord
    template_name = "background.html"

    def get_queryset(self):
        result = BackGroundWord.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_backgroundword w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result

class GirlView(generic.ListView):
    model = GirlWord
    template_name = "girl.html"

    def get_queryset(self):
        result = GirlWord.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_girlword w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result

