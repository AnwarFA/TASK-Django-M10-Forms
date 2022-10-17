from django import forms
from .models import StoreItem
class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ["name", "description", "Kind", "Price"]