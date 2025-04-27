from django import forms
from .models import Listening

class ListeningForm(forms.ModelForm):
    class Meta:
        model = Listening
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional'}),
            'category': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }