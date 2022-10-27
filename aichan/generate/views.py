from django.views import generic

from .models import Word
from .models import Type

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.TemplateView):
    model = Word
    template_name = "generate.html"

    def get_queryset(self):
        result = Word.objects.raw('SELECT w.id,w.word,w.count,t.name FROM Word w INNER JOIN TYPE t ON w.id=t.id order_by t.id')
        return result
