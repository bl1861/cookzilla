from django import forms
 
class UserForm(forms.Form):
    username = forms.CharField(label='inputUsername', max_length=40)
    password = forms.CharField(label='inputPassword', max_length=40)

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    pwd = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    file = forms.FileField(required=False)