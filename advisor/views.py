# advisor/views.py
from django.shortcuts import render

def advisor_home(request):
    materials = [
        {"name": "Bamboo", "cost": 50},
        {"name": "Recycled Steel", "cost": 70},
        {"name": "Fly Ash Concrete", "cost": 55},
        {"name": "Reclaimed Wood", "cost": 60},
        {"name": "Low-VOC Paints", "cost": 20},
        {"name": "Insulated Concrete Forms", "cost": 65},
    ]
    construction_types = [
        {"value": "villa", "label": "Villa"},
        {"value": "flats", "label": "Flats / Apartments"},
        {"value": "company", "label": "Company / Office Buildings"},
        {"value": "individual_home", "label": "Individual Homes"},
        {"value": "other", "label": "Other"},
    ]
    warranties = [
        {"value": "10year", "label": "10 Year"},
        {"value": "15year", "label": "15 Years"},
        {"value": "25year", "label": "25 Years"},
        {"value": "none", "label": "No Warranty"},
    ]
    context = {
        "materials": materials,
        "construction_types": construction_types,
        "warranties": warranties,
    }
    return render(request, 'advisor.html', context)
