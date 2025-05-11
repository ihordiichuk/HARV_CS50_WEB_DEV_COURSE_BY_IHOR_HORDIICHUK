from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional'}),
            # 'category': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }