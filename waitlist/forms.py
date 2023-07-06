from django import forms
from formtools.wizard.forms import ManagementForm

from .models import UserData, UserDetail


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['phone', 'state']

    def __init__(self, *args, **kwargs):
        super(UserDetailForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})


class WaitListForm(ManagementForm, UserDataForm, UserDetailForm):

    def send_mail(self):
        pass

    pass
