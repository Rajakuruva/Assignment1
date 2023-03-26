from django.shortcuts import render

# Create your views here.

def Disticts(request):
    return render(request,'Disticts.html')

def Rayal(request):
    return render(request,'Rayal.html')

def Kosta(request):
    return render(request,'Kosta.html')