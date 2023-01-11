from django.views import generic

class IdentifyView(generic.TemplateView):
    template_name = "identify.html"
