from django import forms
from address.models import AddressField
from .models import Church
from user.models import User


class AddChurchForm(forms.ModelForm):

    class Meta:
        model = Church
        address = AddressField()
        fields = ('name', 'address', 'picture', 'description', 'pastor_name', 'phone')
