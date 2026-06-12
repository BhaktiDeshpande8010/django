from django.forms import ModelForm
from .models import person

class personform(ModelForm):
    class Meta:
        mode=person
        fields='__all__'