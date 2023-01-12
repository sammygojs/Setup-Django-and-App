from django.http import HttpResponse 

def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

from django.views import View 

class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 