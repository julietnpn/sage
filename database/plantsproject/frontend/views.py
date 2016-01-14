from django.http import HttpResponse

from .models import Plant

def index(request):
	#name = Plant.objects.

	return HttpResponse("hello")