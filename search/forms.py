from django import forms

class SearchForm(forms.Form):
	keyword = forms.CharField(label='keyword', max_length=40)
	search_type = forms.CharField(label='search_type', max_length=40)