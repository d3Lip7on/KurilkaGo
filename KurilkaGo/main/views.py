from django.shortcuts import render

# Create your views here.

def index(request):
    data= {
        "title": "KurilkaGo",
        "values": ["some", "value", "some", "value", "some", "value"]
    }
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')