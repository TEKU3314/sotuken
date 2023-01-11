from django import forms
from download.models import Image

class ModifyForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"