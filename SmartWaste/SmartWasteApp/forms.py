
from django.forms import ModelForm
from SmartWasteApp.models import BinTable


class BinForm(ModelForm):
    class Meta:
        model=BinTable
        fields=['BinName','BinPlace']