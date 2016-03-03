from django import forms
from .models import Plant

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	latinName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-latin-name'}), label='latin name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-common-name'}), label='common name', label_suffix='')


class UpdateForm(forms.Form):
	text= forms.CharField(widget=forms.TextInput(attrs={'id': 'new-attribute-text'}), label='text', label_suffix='')
	select = forms.ModelChoiceField(queryset=Plant.objects.none(),label="select", empty_label="(Nothing)")
	multi = forms.ModelMultipleChoiceField(queryset=Plant.objects.none(), label="multi")

		