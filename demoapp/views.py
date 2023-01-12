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

def main(request):
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

#path parameter
def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 


#query parameter
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
