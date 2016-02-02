from django import forms

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	latinName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-latin-name'}), label='latin name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-common-name'}), label='common name', label_suffix='')

class EditPlantForm(forms.Form):
	characteristics = forms.CharField(label='characteristics');