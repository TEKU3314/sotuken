from django.views import generic
import logging

from .models import Word
from .models import Type

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.ListView):
    model = Word
    template_name = "generate.html"

    def get_queryset(self):
        result = Word.objects.raw('SELECT w.id,w.word,w.word_en,w.count,t.name FROM generate_word w INNER JOIN generate_type t ON w.typeid_id=t.id ORDER BY t.id')
        return result
