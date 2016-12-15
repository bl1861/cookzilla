from django import forms



class ReportForm(forms.Form):

    report_text = forms.CharField(label="report_text", max_length=300)
    report_pic = forms.FileField(required=False)