from django import forms
 
class UserForm(forms.Form):
    username = forms.CharField(label='inputUsername', max_length=40)
    password = forms.CharField(label='inputPassword', max_length=40)

class UploadFileForm(forms.Form):
    signup_username = forms.CharField(max_length=50)
    signup_password = forms.CharField(max_length=50)
    signup_nickname = forms.CharField(max_length=50)
    signup_desc = forms.CharField(max_length=300)
    signup_file = forms.FileField(required=False)
    signup_photo = forms.FileField(required=False)