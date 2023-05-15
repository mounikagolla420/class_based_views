from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from app.forms import *
def fbv_string(request):
    return HttpResponse('this is rendered fbv page')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('data is intereted successfully')

 # FBV for returning HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')


class cbv_html(View):
    def get(self, request):
        return render(request,'cbv_html.html')

# Handling forms by using FBV

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


    return render(request,'fbv_form.html',d)

# Handling forms by using CBV

class cbv_form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)

    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        return HttpResponse('data is inserted')

    

            
















