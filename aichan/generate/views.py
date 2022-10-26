from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.TemplateView):
    template_name = "generate.html"
