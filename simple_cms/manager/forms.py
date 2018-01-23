from django import forms
from manager.models import Template

class NewTemplateForm(forms.Form):
	name = forms.CharField(label="Name", max_length=150)
	path = forms.FilePathField(path="manager/templates/manager/")


class NewArticleForm(forms.Form):
	title = forms.CharField(label="Title", max_length=150)
	link = forms.CharField(label="Link", max_length=200)
	template = forms.ModelChoiceField(label="Template", queryset=Template.objects.all())

	def clean_link(self):
		data = self.cleaned_data['link']
		if " " in data:
			raise forms.ValidationError("Spaces are not allowed in the link!")

		return data