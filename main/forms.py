from django import forms
 
class UserForm(forms.Form):
    username = forms.CharField(label='inputUsername', max_length=40)
    password = forms.CharField(label='inputPassword', max_length=40)
