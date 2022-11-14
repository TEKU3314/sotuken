from django.views import generic
from django.http import JsonResponse
import logging

from .models import Word
from .models import Type

logger = logging.getLogger(__name__)

def make(request):
    #画像生成処理
    
    
    number1 = request.POST.get('number1')
    d = {
        'plus': number1,
    }
    return JsonResponse(d)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.ListView):
    model = Word
    template_name = "generate.html"

    def get_queryset(self):
        result = Word.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_word w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result
