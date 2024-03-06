from django.forms import ModelForm
from .models import *
from django.forms import ModelForm
from .models import forum

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        exclude = ['email']  # Exclude the 'email' field from the form
    def clean_topic(self):
        return self.cleaned_data['topic'].upper()
 
class CreateInDiscussion(ModelForm):
    
    class Meta:
        model= Discussion
        exclude = ['email'] 
    def __str__(self):
        return str(self.forum)    