from django.shortcuts import render
import requests
from threading import Timer

# Create your views here.
from django.http import HttpResponse
from .models import allStatus


def index(request):
    all_status = allStatus.object.all()
    return render(request, 'url.html', {'result':all_status})
def startTesting(request) : 
    text = request.POST['content']

    checkurl(text)


def checkurl(url):
    start = True
    try :
        request = requests.get(url, timeout=5)
        status = requests.head(url,timeout=5 ).status_code
        response = requests.get(url)
        if(status == 200):
           a = allStatus(content ='status : Active '  + 'response Time : '+ response.elapsed )
           a.save()

        else :
            a = allStatus(content ='status : INActive' )
            a.save()

        
    except (requests.ConnectionError, requests.Timeout) as exception:
	    a = allStatus(content ="No internet connection.")


    # r = Timer(3.0, checkurl(url))
    # r.start(start)