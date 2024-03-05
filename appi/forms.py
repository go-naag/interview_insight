from django.forms import ModelForm
from .models import *
 
from django.forms import ModelForm
from .models import forum

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        exclude = ['email']  # Exclude the 'email' field from the form

 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"