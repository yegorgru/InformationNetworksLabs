from django.forms import ModelForm
from . import models


class CoinForm(ModelForm):
    class Meta:
        model = models.Coin
        fields = ["par", "currency", "year", "material", "weight", "diameter", "price", "description", "image_obverse", "image_reverse"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["par"].widget.attrs.update({'class': 'form-control', 'placeholder': 'par', 'min': '1', 'max': '1000000'})
        self.fields["currency"].widget.attrs.update({'class': 'form-control', 'placeholder': 'currency'})
        self.fields["year"].widget.attrs.update({'class': 'form-control', 'placeholder': 'year', 'min': '-50000', 'max': '50000'})
        self.fields["material"].widget.attrs.update({'class': 'form-control', 'placeholder': 'material'})
        self.fields["weight"].widget.attrs.update({'class': 'form-control', 'placeholder': 'weight', 'min': '0', 'max': '10000'})
        self.fields["diameter"].widget.attrs.update({'class': 'form-control', 'placeholder': 'diameter', 'min': '0', 'max': '10000'})
        self.fields["price"].widget.attrs.update({'class': 'form-control', 'placeholder': 'price', 'min': '1', 'max': '1000000'})
        self.fields["description"].widget.attrs.update({'class': 'form-control', 'placeholder': 'description'})
        self.fields["image_obverse"].widget.attrs.update({'class': 'm-3'})
        self.fields["image_reverse"].widget.attrs.update({'class': 'm-3'})


class CreateEditCoinForm(CoinForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["par"].required = True
        self.fields["currency"].required = True
        self.fields["year"].required = True
        self.fields["material"].required = False
        self.fields["weight"].required = False
        self.fields["diameter"].required = False
        self.fields["price"].required = True
        self.fields["description"].required = False
        self.fields["image_obverse"].required = False
        self.fields["image_reverse"].required = False


class SearchCoinForm(CoinForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["par"].required = False
        self.fields["currency"].required = False
        self.fields["year"].required = False
        self.fields["material"].required = False
        self.fields["weight"].required = False
        self.fields["diameter"].required = False
        self.fields["price"].required = False
        self.fields["description"].required = False
        self.fields["image_obverse"].required = False
        self.fields["image_reverse"].required = False
