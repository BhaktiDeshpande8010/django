# from django.forms import ModelForm
# from .models import person

# class personform(ModelForm):
#     class Meta:
#         mode = person
#         fields='__all__'
#     #  fields = ['fullname', 'email', 'password', 'contact', 'address']

from django.forms import ModelForm
from .models import person

class personform(ModelForm):
    class Meta:
        model = person
        fields = '__all__'