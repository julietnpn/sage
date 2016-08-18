
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms import ModelForm, modelform_factory
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from plants.models import PlantFoodProd, Plant, PlantMedicinalsProd, PlantCulturalAndAmenityProd, PlantBiochemicalMaterialProd, PlantRawMaterialsProd, PlantMineralNutrientsProd
from .forms import Human_Needs, Address, Plants, Support, IDForm, finalPage
from django.core.urlresolvers import reverse
from django import forms
from django.core.context_processors import csrf
from django.views.generic.edit import UpdateView
from .models import ID_Table, Human_Needs_Library, SPC_Project, Chosen_Plants, Chosen_Human_Needs


UNIVERSALID = 1 #GLOBAL ID VARIABLE




#VIEW FOR MAP PLACEMENT
def PlantPlacement(request):
    addressvalues = SPC_Project.objects.order_by('id')
    currentaddress = ""

    for i in range(0, len(addressvalues), 1):
        if (addressvalues[i].user_id == UNIVERSALID):  # ADD ACTUAL USER ID HERE!!!
            currentaddress = addressvalues[i].address
            break

    #context = {'addressvalues': addressvalues}
    if request.method == 'POST':
        coordinates = request.POST.get('test', '')


        coordinatearray = []
        i = 0
        while True:
            index = coordinates.find(",", i)
            if index == -1:
                coordinatearray.append(coordinates[i:len(coordinates)])
                break
            coordinatearray.append(coordinates[i:index])
            i = index + 1

        for j in range(0, len(addressvalues), 1):
            if (addressvalues[j].user_id == UNIVERSALID and addressvalues[j].id > 0):
                addressvalues[j].polyculture_coordinates = ""
                addressvalues[j].polyculture_coordinates = coordinates
                addressvalues[j].save()
                break
        #convert string back to array
        return HttpResponseRedirect('/composer/')
    else:
        #form = Address()
        return render(request, 'composer/map.html', {"value": currentaddress})

# VIEW FOR SUPPORT SPECIES
def FindSupport(request):
    if request.method == 'POST':

        form = Support(request.POST)
        if form.is_valid():
            selectedPlants = form.cleaned_data.get('supportchoices')
            selectedId = map(int, selectedPlants)

            for i in range(0, len(selectedId), 1):
                newdata = Chosen_Plants(project_id=UNIVERSALID, plant_id=selectedId[i], key_species=False)
                newdata.save()

        return HttpResponseRedirect('/composer/next/')
    else:
        form = Support()
        return render(request, 'composer/support.html', {'form': form})


# VIEW FOR KEY SPECIES
def FindProducts(request):
    existingobjects = Chosen_Plants.objects.order_by('id')
    #a = request.session.get('a', None)

    # Task 4: Store each task into the Chosen_Plants_Table
    if request.method == 'POST':

        form = Plants(request.POST)
        if form.is_valid():
            selectedPlants = form.cleaned_data.get('plantrec')
            selectedId = map(int, selectedPlants)

            for i in range(0, len(existingobjects), 1):
                if (existingobjects[i].project_id == UNIVERSALID):
                    deletedEntry = Chosen_Plants.objects.get(id=existingobjects[i].id)
                    deletedEntry.delete()

            for i in range(0, len(selectedId), 1):
                newdata = Chosen_Plants(project_id=UNIVERSALID, plant_id= selectedId[i], key_species= True)
                newdata.save()


        return HttpResponseRedirect('/composer/support/')
    else:
        existingList = []

        form = Plants()
        return render(request, 'composer/Plants.html', {'form': form})
        #return render_to_response('composer/Plants.html', args)
    #add plants into tuple depending on what user chooses


# VIEW FOR HUMAN NEEDS
def UserInsert(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #question = get_object_or_404(Human_Needs_Library, pk = 2)
    #selected_choice = question.choice_set.get(pk=request.POST['products'])

    chosenobjects = Chosen_Human_Needs.objects.order_by('id')
    largestid = UNIVERSALID
    #for i in range(0, len(objects), 1):  # finds largest project id value
    #    currentnumber = objects[i].project_id
    #    if currentnumber > largestid:
    #        largestid = currentnumber
    #largestid += 1

    #largestid = 1
    print request.method
    if request.method == 'POST': #add project number function

        form = Human_Needs(request.POST)

        #print largestid
        if form.is_valid():
            picked = form.cleaned_data.get('picked')


            # add functionality

            for i in range(0, len(chosenobjects), 1):
                if(chosenobjects[i].project_id == largestid):
                    deletedEntry = Chosen_Human_Needs.objects.get(id= chosenobjects[i].id)
                    deletedEntry.delete()

            picked = map(int, picked)
            for i in range(0, len(picked), 1):
                newdata = Chosen_Human_Needs(project_id=largestid, human_need_lib_id=picked[i])
                newdata.save()
            #newForm = Plants()
            print 'database created'
            #return render(request, 'composer/Plants.html', {'form': newForm})
        else:
            print 'database not created'


        #newForm = Plants()
        #return render_to_response('composer/Plants.html', {'form': newForm}, context_instance=RequestContext(request))
        return HttpResponseRedirect('/composer/plants/')

        #return render(request, 'composer/enter.html', {'form': form})


    else:
        existingList = []
        for i in range(0, len(chosenobjects), 1):
            if (chosenobjects[i].project_id == UNIVERSALID):
                existingList.append(chosenobjects[i].human_need_lib_id)
        form = Human_Needs(initial={'picked': existingList})
        return render(request, 'composer/enter.html', {'form': form})




# VIEW FOR ID PLACEHOLDER
def EnterID(request):
    if request.method == 'POST':
        IDtext = str(request.POST.get('textfield'))
        global UNIVERSALID
        UNIVERSALID = int(IDtext)
        newdata = ID_Table(id_Value= UNIVERSALID, id=1)
        newdata.save()
        return HttpResponseRedirect('/composer/address')
    else:
        form = IDForm()
        return render(request, 'composer/id.html', {'form': form})


# VIEW FOR ENTERING ADDRESS
def EnterAddress(request):
    addresstext = str(request.POST.get('textfield'))

    existingaddress = SPC_Project.objects.order_by('id')

    if request.method == 'POST':  # add project number function

        #form = Address(request.POST)
        #if form.is_valid():

        for i in range(0, len(existingaddress), 1):
            if (existingaddress[i].user_id == UNIVERSALID):
                deletedEntry = SPC_Project.objects.get(id=existingaddress[i].id)
                deletedEntry.delete()

        newAddress = SPC_Project(user_id=UNIVERSALID, address=addresstext)
        newAddress.save()


        #else:
            #print 'address not created'
            # print form

        return HttpResponseRedirect('/composer/maps')
    else:
        existingList = []
        for i in range(0, len(existingaddress), 1):
            if (existingaddress[i].user_id == UNIVERSALID):
                existingList.append(existingaddress[i].address)
        form = Address(initial={'addresstext': existingList})
        return render(request, 'composer/Address.html', {'form': form})


# VIEW FOR FINAL PAGE
def Return(request):
    form = finalPage()
    return render(request, 'composer/next.html', {'form': form})






