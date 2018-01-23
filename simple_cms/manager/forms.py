from django import forms

class NewTemplateForm(forms.Form):
	name = forms.CharField(label="Name", max_length=150)
	path = forms.FilePathField(path="manager/templates/manager/")