from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import Plant, Transactions, Actions
from .forms import AddPlantForm, EditPlantForm


def cardview(request):	
	plant_list = Plant.objects.filter(genus__startswith='Ag')
	context = {
		'plant_list': plant_list,
	}
	return render(request, 'frontend/cardview.html', context)

def editPlant(request, plantId=None):
	if request.method == 'POST':
		form = EditPlantForm(request.POST)
		if form.is_valid():

			return HttpResponseRedirect('POST')
	else:
		form = EditPlantForm()
		context = {
			'plant': Plant.objects.filter(id=8665)[0]
		}
		redirectURL = 'frontend/editplant.html'
		return render(request, redirectURL, context)

def addPlant(request):
	if request.method == 'POST':
		form = AddPlantForm(request.POST)
		if form.is_valid():
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

			redirectURL = '/home/edit/' + str(transaction.id)
			return HttpResponseRedirect(redirectURL)
	else:
		form = AddPlantForm()
		plant_list = Plant.objects.filter(genus__startswith='Ag')
		context = {
			'form': form,
			'plant_list': plant_list,
		}
		return render(request, 'frontend/cardview.html', context)