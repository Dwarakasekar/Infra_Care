# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("hello Prototype Infra-care")
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def clientpage(request):
    return render(request, 'client.html')

def orgpage(request):
    return render(request, 'org.html')

def cp_view(request):
    return render(request, 'create.html')

def cc_view(request):
    return render(request, 'cc.html')

# def climate_view(request):
#     return render(request, 'climate.html')

# def cs_view(request):
#     return render(request, 'support.html')