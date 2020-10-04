from django import forms
from . models import User, Company

class NewUsersLogin(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


class NewCompany(forms.ModelForm):
    class Meta():
        model = Company
        fields = '__all__'