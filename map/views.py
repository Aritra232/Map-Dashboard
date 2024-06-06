from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'templates/index.html')

def reverse_geocoding(request):
    if request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
        # Perform reverse geocoding here using lat and lon
        # Dummy response for demonstration
        response_data = {'display_name': 'Dummy Location Name'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request'})
