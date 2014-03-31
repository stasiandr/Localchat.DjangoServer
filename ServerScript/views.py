from django.shortcuts import HttpResponse
from ServerScript.models import ChatPoint
from django.core import serializers

# Create your views here.
def parse(request, name):
	if name == 'setChat':
		x_ = request.GET['x']
		y_ = request.GET['y']
		chat_name_ = request.GET['chat_name']
		query = ChatPoint(chat_name = chat_name_, x=x_, y=y_)
		query.save();
		return HttpResponse("OK")
	else:
		return HttpResponse("lalka")

def print_array(request):

	return HttpResponse(serializers.serialize("json", ChatPoint.objects.all()))