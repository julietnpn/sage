from django.shortcuts import render

# Create your views here.
from login.forms import *
from django.contrib.auth.models import User
from login.models import AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import *
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['firstname'],
            last_name=form.cleaned_data['lastname'],
            )
            auth_user = AuthUser.objects.get(username=form.cleaned_data['username'])
            auth_user.affiliation=form.cleaned_data['affiliation']
            auth_user.experience=form.cleaned_data['experience']
            auth_user.interests=form.cleaned_data['interests']
            auth_user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = {'form': form}
    return render(request,'registration/register.html', variables)
 
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
    userName = User.objects.get(id=userID).username
    user = AuthUser.objects.get(username=userName)
    context = {
        'userName' : userName,
        'firstName' : user.first_name,
        'lastName' : user.last_name,
        'affiliation' : user.affiliation,
        'experience' : user.experience,
        'interests' : user.interests,
    }
    return render(request, 'user_profile.html', context)