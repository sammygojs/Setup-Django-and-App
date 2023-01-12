from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('class', views.MyView.as_view()),
    path('request_data', views.main),

    #path parameter   
    path('<name>/<id>', views.pathview, name='pathview'), 
    #query parameter
    path('getuser/', views.qryview, name='qryview') 

]
