from django.views import generic
from django.http import JsonResponse
import json

class ModifyView(generic.TemplateView):
    template_name = "modify.html"

def ajax_file_send(request):
    print("OK")
    file = request.FILES['uploadfile']
    print(file)

    #↓画像修正プログラミング
    filename = ''
    
    #↑画像修正プログラミング

    d = {
        'result': filename,
    }
    return JsonResponse(d)
