from django.shortcuts import render

def disaster_toolkit(request):
    # Sample context data - in production you'd fetch real weather data
    context = {
        'weather_alerts': [
            {'type': 'Heavy Rain', 'severity': 'high'},
            {'type': 'Flood Warning', 'severity': 'critical'},
        ],
        'nearby_resources': {
            'hospitals': [
                {'name': 'City General Hospital', 'distance': '2.3 km'},
                {'name': 'Emergency Care Center', 'distance': '5.1 km'},
            ],
            'fire_stations': [
                {'name': 'Central Fire Station', 'distance': '3.7 km'},
            ]
        }
    }
    return render(request, 'disaster_toolkit.html', context)