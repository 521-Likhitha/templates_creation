from django.shortcuts import render

# Create your views here.
def likki(request):
    return render(request,'likki.html')

def saha(request):
    return render(request,'saha.html')
