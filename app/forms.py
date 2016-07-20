from django import forms

from app.models import Quantity

class CreateSubAssembly(forms.Form):


    class Meta:
        model = Quantity
        fields = ['part', 'quantity', 'assembly']
