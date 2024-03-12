from django.shortcuts import render

# Create your views here.
from .models import vehicles

def vehicle_list(request):
    # vehicles_data = vehicles.objects.all()
    # return render(request, 'vehicle_list.html', {'vehicles_data': vehicles_data})

    sort_by = request.GET.get('sort_by', 'name')  # Default sorting by name if no option selected
    print("Sort by:", sort_by)  # Add this line for debugging
    if sort_by == 'price':
        vehicles_data = vehicles.objects.all().order_by('vehicles_price')
    else:
        vehicles_data = vehicles.objects.all().order_by('vehicles_name')
    
    return render(request, 'vehicle_list.html', {'vehicles_data': vehicles_data, 'sort_by': sort_by})