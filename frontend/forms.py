from django import forms
from plants.models import Plant, EndemicStatus, TheFamilyCommonName, TheFamily
from django.apps import apps

class AddPlantForm(forms.Form):
	#not sure we need ID's anymore
	scientificName = forms.CharField(widget=forms.TextInput(attrs={'id':'add-plant-scientifc-name', 'class': 'formtxt'}), label='scientific name', label_suffix='')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'id':'add-plant-common-name','class': 'formtxt'}), label='common name', label_suffix='')


class UpdateAttributeForm(forms.Form):
	text= forms.CharField(widget=forms.TextInput(), required=False, label='text', label_suffix='')
	multi = forms.CharField(widget=forms.SelectMultiple, required=False)
	select = forms.ModelChoiceField(queryset=None, label="select", empty_label="Loading...", required=False)
	reference = forms.CharField(widget=forms.TextInput(), required=False, label='Reference')

	def __init__(self, *args, **kwargs):
		class_name = kwargs.pop('class_name')
		if class_name == "Plant":
			values = Plant.objects.none()
		else:
			cls_model = apps.get_model('plants', class_name)
			values = cls_model.objects.values_list("id", flat = True)
		super(UpdateAttributeForm, self).__init__(*args, **kwargs)
		self.fields['select'].queryset = values


class UpdatePlantNamesForm(forms.Form):
	# genus = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-genus'}), label='Genus')
# 	species = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-species'}), label='Species')
# 	variety = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-variety'}), label='Variety')
# 	subspecies = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-subspecies'}), label='Subspecies')
# 	cultivar = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-cultivar'}), label='Cultivar')
	scientificName = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-scientificName'}), label='Scientific Name')
	commonName = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-commonName'}), label='Common Name')
	#familyCommonName =forms.CharField(widget=forms.TextInput(attrs={'id': 'input-familyCommonName'}), label='Family Common Name')
	#family = forms.CharField(widget=forms.TextInput(attrs={'id': 'input-family'}), label='Family')
	family = forms.ModelChoiceField(queryset=TheFamily.objects.values_list("value", flat=True).distinct(), label='Family', widget=forms.Select(attrs={'class':'formselect'}))
	familyCommonName = forms.ModelChoiceField(queryset=TheFamilyCommonName.objects.values_list("value", flat=True).distinct(), label='Family Common Name', widget=forms.Select(attrs={'class':'formselect'}))
	endemicStatus = forms.ModelChoiceField(queryset=EndemicStatus.objects.all().distinct(), label='Endemic Status', widget=forms.Select(attrs={'class':'formselect'}))
