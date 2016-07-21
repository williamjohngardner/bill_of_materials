from django import forms

from app.models import SubAssemblyQuantity

class CreateSubAssembly(forms.Form):

    class Meta:
        model = SubAssemblyQuantity
        fields = ['part', 'quantity', 'assembly']
