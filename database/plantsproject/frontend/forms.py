from django import forms
from .models import Plant, EndemicStatus
from django.apps import apps

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	latinName = forms.CharField(widget=forms.TextInput(attrs={'id':'add-plant-latin-name', 'class': 'formtxt'}), label='latin name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'id':'add-plant-common-name','class': 'formtxt'}), label='common name', label_suffix='')

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

class UpdatePlantNamesForm(forms.Form):
	genus = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-genus'}), label='Genus')
	species = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-species'}), label='Species')
	variety = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-variety'}), label='Variety')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-commonName'}), label='Common Name')
	familyCommonName =forms.CharField(widget=forms.TextInput(attrs={'id': 'input-familyCommonName'}), label='Family Common Name')
	family = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-family'}), label='Family')
	endemicStatus = forms.ModelChoiceField(queryset=EndemicStatus.objects.all().distinct(), label='EndemicStatus')
