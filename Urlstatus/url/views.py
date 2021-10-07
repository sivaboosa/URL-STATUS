from django.shortcuts import render
import requests
from threading import Timer
from django.http  import HttpResponseRedirect
import datetime

# Create your views here.
from django.http import HttpResponse
from .models import allStatus


def index(request):
    all_status = allStatus.objects.all()
    return render(request, 'url.html', {'result':all_status})
def startTesting(request) : 
    text = request.POST['content']

    checkurl(text)
    return HttpResponseRedirect('/url/')


def checkurl(url):
    start = True
    try :
        request = requests.get(url, timeout=5)
        status = requests.head(url,timeout=5 ).status_code
        response = requests.get(url)
        if(status == 200):
           time =str( response.elapsed )
           a = allStatus(content ='Requested Url : '+ url +' Status  : Active '  + 'Response Time : '+time )
        
           a.save()

        else :
            a = allStatus(content ='Requested Url : '+ url +' Status : INActive' )
            a.save()

        
    except (requests.ConnectionError, requests.Timeout) as exception:
	    a = allStatus(content ="No internet connection.")
    return ''


    # r = Timer(3.0, checkurl(url))
    # r.start(start)