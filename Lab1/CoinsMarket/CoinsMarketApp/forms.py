from django.forms import ModelForm
from . import models


class CreateCoinForm(ModelForm):
    class Meta:
        model = models.Coin
        fields = ["par", "currency", "year", "material", "weight", "diameter", "price", "description", "image_obverse", "image_reverse"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["par"].widget.attrs.update({'class': 'form-control', 'placeholder': 'par', 'min': '1'})
        self.fields["currency"].widget.attrs.update({'class': 'form-control', 'placeholder': 'currency'})
        self.fields["year"].widget.attrs.update({'class': 'form-control', 'placeholder': 'year'})
        self.fields["material"].widget.attrs.update({'class': 'form-control', 'placeholder': 'material'})
        self.fields["weight"].widget.attrs.update({'class': 'form-control', 'placeholder': 'weight', 'min': '0'})
        self.fields["diameter"].widget.attrs.update({'class': 'form-control', 'placeholder': 'diameter', 'min': '0'})
        self.fields["price"].widget.attrs.update({'class': 'form-control', 'placeholder': 'price', 'min': '1'})
        self.fields["description"].widget.attrs.update({'class': 'form-control', 'placeholder': 'description'})
        self.fields["image_obverse"].widget.attrs.update({'class': 'm-3'})
        self.fields["image_reverse"].widget.attrs.update({'class': 'm-3'})


