from django import forms

from ratings.models import RatingOrder


class RatingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["order"].widget = forms.HiddenInput()
        self.fields["user"].widget = forms.HiddenInput()


class Meta:
    model = RatingOrder
    fields = ["order", "testimonial", "user", "order_rating"]

def clean(self):
    cleaned_data = super().clean()
    return cleaned_data