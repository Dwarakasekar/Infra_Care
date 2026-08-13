from django.shortcuts import render

# Create your views here.

# View for the customer support page
def track_project_view(request):
    return render(request, 'track.html')
