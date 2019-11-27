from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
def index(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':Webpages_list}
    my_dict = {'insert_me':"hello a'm from views.py"}
    return render(request, 'first.app/index.html', context=my_dict)
# Create your views here.
