from django.shortcuts import render

# Create your views here.

def customer_support_view(request):
    return render(request, 'support.html')
