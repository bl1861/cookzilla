from django import forms
 
class NewGroupForm(forms.Form):
    groupname = forms.CharField(max_length=70)

class UploadFileForm(forms.Form):
    signup_username = forms.CharField(max_length=50)
    signup_password = forms.CharField(max_length=50)
    signup_nickname = forms.CharField(max_length=50)
    signup_desc = forms.CharField(max_length=300)
    signup_file = forms.FileField(required=False)