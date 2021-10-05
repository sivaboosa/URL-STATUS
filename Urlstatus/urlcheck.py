import requests
from threading import Timer
url1 = 'https://www.youtube.com/watch?v=ovql0Ui3n_I'
def checkurl(url):
    start = True
    try :
        request = requests.get(url, timeout=5)
        status = requests.head(url,timeout=5 ).status_code
        response = requests.get(url)
        if(status == 200):
            print('status : Active' , 'response Time : ', response.elapsed )

        else :
            print('status : INActive' )

        
    except (requests.ConnectionError, requests.Timeout) as exception:
	    print("No internet connection.")

    r = Timer(3.0, checkurl(url))
    r.start(start)

checkurl(url1)