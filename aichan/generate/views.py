from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenetateView(generic.TemplateView):
    template_name = "generate.html"

class GenerateConfirmView():
    template_name = "generate_confirm.html"

class GenerateFinishView():
    template_name = "generate_finish.html"
