from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':"hello a'm from views.py"}
    return render(request, 'first.app/index.html', context=my_dict)
# Create your views here.
