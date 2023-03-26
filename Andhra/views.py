from django.shortcuts import render

# Create your views here.


def States(request):
    return render(request,'States.html')

def Festivals(request):
    return render(request,'Festivals.html')

def History(request):
    return render(request,'History.html')

def Culture(request):
    return render(request,'Culture.html')