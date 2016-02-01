from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Plant

#@login_required
def cardview(request):	
	plant_list = Plant.objects.filter(genus__startswith='Ag')
	context = {
		'plant_list': plant_list,
	}
	return render(request, 'frontend/cardview.html', context)

def editPlant(request, genus=None, species=None, variety=None, commonName=None, imgUrl=None):
	#genus = latinName.split()[0]
	#species = latinName.split()[1]
	#variety = latinName.split()[2]

	#transaction = Transactions(users_id=1, transaction_type='INSERT', ignore=False)
	#transaction.save()
	#actions = []
	#actions.append(Actions(transaction=transaction.id, action_type="INSERT", property='genus', value=genus))
	#actions.append(Actions(transaction=transaction.id, action_type="INSERT", property='species', value=species))
	#actions.append(Actions(transaction=transaction.id, action_type="INSERT", property='variety', value=variety))
	#actions.append(Actions(transaction=transaction.id, action_type="INSERT", property='common_name', value=commonName))
	#actions.append(Actions(transaction=transaction.id, action_type="INSERT", property='img_url', value=imgUrl))
	#Actions.objects.bulk_create(actions)
	context = {
	#	'plant_id': transaction.plant_id,
	}
	return render(request, 'frontend/editplant.html', context)