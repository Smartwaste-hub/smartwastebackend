
from django.forms import ModelForm
from SmartWasteApp.models import BinTable, ProductTable


class BinForm(ModelForm):
    class Meta:
        model=BinTable
        fields=['BinName','BinPlace']

class ProductForm(ModelForm):
    class Meta:
        model=ProductTable
        fields=['ProductName','Point','Image','Description']
