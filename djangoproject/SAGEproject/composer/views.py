
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms import ModelForm, modelform_factory
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from plants.models import Human_Needs_Library, PlantFoodProd, SPC_Project, Chosen_Plants, Chosen_Human_Needs, Plant, PlantMedicinalsProd, PlantCulturalAndAmenityProd, PlantBiochemicalMaterialProd, PlantRawMaterialsProd, PlantMineralNutrientsProd
from .forms import Human_Needs, Address, Plants, Support, IDForm
from django.core.urlresolvers import reverse
from django import forms
from django.core.context_processors import csrf
from django.views.generic.edit import UpdateView
from .models import ID_Table


UNIVERSALID = 1 #GLOBAL ID VARIABLE


class LocationUpdateView(UpdateView):
    print 'LOCATION UPDATE'
    model = Chosen_Human_Needs
    template_name = 'composer/Plants.html'
    form_class = Plants
    success_url = '/composer/next/'

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



def Sample(request):
    latest_choice = Human_Needs_Library.objects.order_by('id')
    context = {'latest_choice': latest_choice}
    return render(request, 'composer/UserInsert.html', context)

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


def EnterAddress(request):
    addresstext = str(request.POST.get('textfield'))
    print addresstext
    existingaddress = SPC_Project.objects.order_by('id')

    if request.method == 'POST':  # add project number function

        #form = Address(request.POST)
        #if form.is_valid():

        for i in range(0, len(existingaddress), 1):
            if (existingaddress[i].user_id == UNIVERSALID):
                deletedEntry = SPC_Project.objects.get(id=existingaddress[i].id)
                print "DELETED"
                deletedEntry.delete()

        newAddress = SPC_Project(user_id=UNIVERSALID, address=addresstext)
        newAddress.save()

        print 'address created'
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


def Return(request):
    return render(request, 'composer/next.html')

def Answer(request, choice_id):
    choice = get_object_or_404(Human_Needs_Library, pk = choice_id)
    try:
        selected_choice = choice.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Human_Needs_Library.DoesNotExist):
        return render(request, 'composer/UserInsert.html', {
            'choice': choice,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        #return HttpResponseRedirect(reverse('composer:Next', args=(choice.id,)))
        return HttpResponseRedirect(reverse('composer:Next', args=(choice.id,)))
        #return render(request, 'composer/next.html')



def Answer1(request):
    if request.method == 'POST':
        #model = Chosen_Human_Needs
        #form = model(request.POST)

        form = Human_Needs(request.POST)
        print "checkpoint"
        if form.is_valid():
            picked = form.cleaned_data.get('list.initial')
            print picked
            # add functionality
            chosen = Chosen_Human_Needs(project_id=1, human_need_lib_id=picked.id)
            chosen.save()
            print "DATABASE CREATED!!!!!!"
        else:
            print "database not created"


    else:
        form = Chosen_Human_Needs
    return render_to_response('composer/next.html', {'form': form}, context_instance = RequestContext(request))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Human_Needs_Library
        exclude = ['picked']

def altAnswer (request):

    if request.method == 'POST':
        #latest_choice = Human_Needs_Library.objects.order_by('id')
        form = ProfileForm(data = request.POST)
        print form.is_valid(), form.errors

        if form.is_valid() == False:
            #print 'REACHED LOOP'
            picked = form.cleaned_data.get('type')
            chosen = Chosen_Human_Needs(project_id=1, human_need_lib_id=picked)
            chosen.save()
        else:
            print "database not created"
    else:
        form = ProfileForm()
    return render_to_response('composer/next.html', {'form': form}, context_instance = RequestContext(request))



def AddRandomResponse (request):
    p = Chosen_Human_Needs( project_id = 1, human_need_lib_id = 1)
    p.save()
    return render(request, 'composer/next.html')


def Next(request, choice_id):
    choice = get_object_or_404(Human_Needs_Library, pk=choice_id)
    return render(request, 'composer/next.html', {'choice': choice})
