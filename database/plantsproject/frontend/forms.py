from django import forms

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	latinName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-latin-name'}), label='latin name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'class': 'formtxt', 'id':'add-plant-common-name'}), label='common name', label_suffix='')

class UpdateFormWithText(forms.Form):
	value = forms.CharField(widget=forms.TextInput(attrs={'id': 'new-attribute-text'}), label='test', label_suffix='')
	#multiValue = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

class UpdateFormWithSelect(forms.Form):
	value = forms.ModelChoiceField(queryset=..., empty_label="(Nothing)")