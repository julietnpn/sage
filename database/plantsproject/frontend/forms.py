from django import forms
from .models import Plant
from django.apps import apps

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	latinName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-latin-name'}), label='latin name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-common-name'}), label='common name', label_suffix='')

class UpdateTextForm(forms.Form):
	text= forms.CharField(widget=forms.TextInput(attrs={'id': 'new-attribute-text'}), label='text', label_suffix='')

class UpdateSelectForm(forms.Form):
	select = forms.ModelChoiceField(queryset=None,label="select", empty_label="Loading...")
	def __init__(self, *args, **kwargs):
		class_name = kwargs.pop('class_name')
		if class_name is "Plant":
			values = Plant.objects.none()
		else:
			cls_model = apps.get_model('frontend', class_name)
			values = cls_model.objects.values_list("id", flat = True)
		super(UpdateSelectForm, self).__init__(*args, **kwargs)
		self.fields['select'].queryset = values

class UpdateMultiForm(forms.Form):
	multi = forms.CharField(widget=forms.SelectMultiple)
