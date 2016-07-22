
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms import ModelForm, modelform_factory
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from plants.models import Human_Needs_Library, PlantFoodProd, SPC_Project, Chosen_Plants, Chosen_Human_Needs, Plant, PlantMedicinalsProd, PlantCulturalAndAmenityProd, PlantBiochemicalMaterialProd, PlantRawMaterialsProd, PlantMineralNutrientsProd
from .forms import Human_Needs, Address, Plants
from django.core.urlresolvers import reverse
from django import forms
from django.core.context_processors import csrf
from django.views.generic.edit import UpdateView


class LocationUpdateView(UpdateView):
    print 'LOCATION UPDATE'
    model = Chosen_Human_Needs
    template_name = 'composer/Plants.html'
    form_class = Plants
    success_url = '/composer/next/'

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
                if (existingobjects[i].project_id == 1):
                    deletedEntry = Chosen_Plants.objects.get(id=existingobjects[i].id)
                    deletedEntry.delete()

            for i in range(0, len(selectedId), 1):
                newdata = Chosen_Plants(project_id=1, plant_id= selectedId[i], key_species= False)
                newdata.save()


        return HttpResponseRedirect('/composer/next/')
    else:
        form = Plants()
        return render(request, 'composer/Plants.html', {'form': form})
        #return render_to_response('composer/Plants.html', args)
    #add plants into tuple depending on what user chooses


def UserInsert(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #question = get_object_or_404(Human_Needs_Library, pk = 2)
    #selected_choice = question.choice_set.get(pk=request.POST['products'])

    chosenobjects = Chosen_Human_Needs.objects.order_by('id')
    largestid = 1
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
        form = Human_Needs()
        return render(request, 'composer/enter.html', {'form': form})



def Sample(request):
    latest_choice = Human_Needs_Library.objects.order_by('id')
    context = {'latest_choice': latest_choice}
    return render(request, 'composer/UserInsert.html', context)

def EnterAddress(request):
    addresstext = str(request.POST.get('textfield'))
    print addresstext, len(addresstext)

    if (addresstext is None) == False:

        newAddress = SPC_Project(user_id=1, address=addresstext)
        newAddress.save()
            #print form
        return render(request, 'composer/next.html')
    else:
        form = Address()
        return render(request, 'composer/Address.html')


def Return(request):
    return render(request, 'composer/enter.html')

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
    return render(request, 'polls/next.html', {'choice': choice})
