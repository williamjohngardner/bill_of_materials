from django import forms
from app.models import Customer, Supplier


class CreateCustomer(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'title', 'company_name', 'phone_number', 'email_address', 'twitter_account', 'web_address', 'street_address', 'city', 'state', 'zip_code', 'country']


class CreateSupplier(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['first_name', 'last_name', 'title', 'company_name', 'phone_number', 'email_address', 'twitter_account', 'web_address', 'street_address', 'city', 'state', 'zip_code', 'country']
