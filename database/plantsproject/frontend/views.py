from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import Plant, Transactions, Actions
from .forms import AddPlantForm, EditPlantForm, SearchPlant


#def cardview(request):	
#	plant_list = Plant.objects.filter(id__gte=8667).order_by('id')
#	context = {
#		'plant_list': plant_list,
#	}
#	return render(request, 'frontend/cardview.html', context)

def editPlant(request, plantId=None):
	if request.method == 'POST':
		form = EditPlantForm(request.POST)
		if form.is_valid():

			return HttpResponseRedirect('POST')
	else:
		form = EditPlantForm()
		context = {
			'plant': Plant.objects.filter(id=8667)[0],
			'test': "THIS IS A GET"
		}
		redirectURL = 'frontend/editplant.html'
		return render(request, redirectURL, context)

def addPlant(request):
	if request.method == 'POST':
		addPlantForm = AddPlantForm(request.POST)
		searchForm = SearchPlant(request.POST)


		if 'add' in request.POST and addPlantForm.is_valid():
			nameArray = str(request.POST["latinName"]).split()
			commonName = request.POST["commonName"]

			# IF EITHER OF THE ABOVE ARE "NONE" RETURN ERRORS!!!!!!!

			genus = None
			species = None
			variety = None

			if len(nameArray) > 0:
				genus = nameArray[0]
			if len(nameArray) > 1:
				species = nameArray[1]
			if len(nameArray) > 2:
				variety = nameArray[2]

			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, transaction_type='INSERT', ignore=False)
			transaction.save()
			#print(transaction.id)
			actions = []
			if genus:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='genus', value=genus))
			if species: 
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='species', value=species))
			if variety:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='variety', value=variety))
			if commonName:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='common_name', value=commonName))
			Actions.objects.bulk_create(actions)

			#add plant id to url below
			return HttpResponseRedirect('/home/edit/1234')
		elif 'search' in request.POST and searchForm.is_valid():
			searchString = request.POST["searchString"]
			return HttpResponseRedirect('/home/edit/' + searchString)

	else:
		add_plant_form = AddPlantForm()
		search_form = SearchPlant()
		plant_list = Plant.objects.filter(id__gte=5000, id__lte=5100).order_by('id')

		context = {
			'addPlantForm': add_plant_form,
			'searchForm': search_form,
			'plant_list': plant_list,
		}
		return render(request, 'frontend/cardview.html', context)