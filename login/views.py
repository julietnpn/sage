from django.shortcuts import render

# Create your views here.
from login.forms import *
from django.contrib.auth.models import User
from login.models import AuthUser
from frontend.models import Transactions, Actions
from plants.models import Plant
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import *
#from django.db.models import get_models, get_app
from django.apps import apps
from django.contrib.auth.hashers import *
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            )
            auth_user = AuthUser.objects.get(username=form.cleaned_data['username'])
            auth_user.first_name=form.cleaned_data['firstname'],
            auth_user.last_name=form.cleaned_data['lastname'],
            auth_user.affiliation=form.cleaned_data['affiliation']
            auth_user.experience=form.cleaned_data['experience']
            auth_user.interests=form.cleaned_data['interests']
            auth_user.is_data_import = False
            auth_user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = {'form': form}
    return render(request,'registration/register.html', variables)

@login_required
def edit_profile(request):
    auth_user = AuthUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            auth_user.email=form.cleaned_data['email']
            auth_user.first_name=form.cleaned_data['firstname']
            auth_user.last_name=form.cleaned_data['lastname']
            auth_user.affiliation=form.cleaned_data['affiliation']
            auth_user.experience=form.cleaned_data['experience']
            auth_user.interests=form.cleaned_data['interests']
            auth_user.save()
            return HttpResponseRedirect('/view_profile')
    else:
        form = EditProfileForm(initial={'email': auth_user.email, 'firstname': auth_user.first_name, 'lastname': auth_user.last_name, 'affiliation': auth_user.affiliation, 'experience': auth_user.experience, 'interests': auth_user.interests})
    variables = {'form': form}
    return render(request,'edit_profile.html', variables)
 
def register_success(request):
    return HttpResponseRedirect('/login')
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render(
    request,
    'home.html',
    {'user': request.user }
    )

@login_required
def view_profile(request):
    userID = request.user.id
    userName = AuthUser.objects.get(id=userID).username
    user = AuthUser.objects.get(username=userName)
    activity = getUserActivity(userID)
    context = {
        'userName' : userName,
        'firstName' : user.first_name,
        'lastName' : user.last_name,
        'email' : user.email,
        'affiliation' : user.affiliation,
        'experience' : user.experience,
        'interests' : user.interests,
        'activity' : getUserActivity(userID)
    }
    return render(request, 'user_profile.html', context)


@login_required
def view_contributor(request, contributorID = None):
    userID = contributorID
    userName = AuthUser.objects.get(id=userID).username
    user = AuthUser.objects.get(username=userName)
    context = {
        'userName' : userName,
        'firstName' : user.first_name,
        'lastName' : user.last_name,
        'affiliation' : user.affiliation,
        'experience' : user.experience,
        'interests' : user.interests,
        'activity' : getUserActivity(userID)
    }
    return render(request, 'user_profile.html', context)

def getUserActivity(userID):
    # get list of transactions made by a user, and we are creating a avtivity context,
    # which is a list of activites that consist of plant name, activity type, property, and its value.     
    transactions = Transactions.objects.filter(users = userID)
    activities = []
    for t in transactions:
        plant_id = t.plants_id
        plant = Plant.objects.get(id=plant_id)
        actions = Actions.objects.filter(transactions_id = t.id)
    
        for a in actions:
            try:
                property_model = next((m for m in apps.get_models() if m._meta.db_table == a.property), None)
                value = property_model.objects.get(id = a.value).value 
            except:
                value = a.value
    
            activity = {
                "plant_name" : plant.get_scientific_name,
                "type" : a.action_type,
                "property" : a.property,
                "value" : value,
                "reference" : a.reference
            }
            activities.append(activity)
    return activities

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            request.user.password = make_password(password1)
            request.user.password = make_password(password2)
            request.user.save()
            return HttpResponseRedirect('/reset')
    else:
        form = PasswordChangeForm()
    variables = {'form': form}
    return render(request,'change_password.html', variables)
    