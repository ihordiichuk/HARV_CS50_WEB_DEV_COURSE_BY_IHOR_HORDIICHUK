from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    """
    Form for creating a new listing. Inherits from Django's ModelForm.
    Fields are automatically mapped from the Listing model.
    """
    class Meta:
        # Link this form to the Listing model
        model = Listing

        # Specify which fields from the model to include in the form
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

        # Customize widgets for certain fields for better UX
        widgets = {
            # Render description as multi-line textarea
            'description': forms.Textarea(attrs={'rows': 4}),

            # Optional field for image URL
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional'}),

            # Optional category field (free text or can be overridden)
            'category': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }