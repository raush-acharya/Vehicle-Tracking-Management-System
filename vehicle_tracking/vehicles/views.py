from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse


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




def calculate_booking_price(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Retrieve the vehicle object from the database
        vehicle = get_object_or_404(vehicles, pk=vehicle_id)

        # Calculate the number of days between start_date and end_date
        # Make sure to convert start_date and end_date to datetime objects
        # Example: start_date = datetime.strptime(start_date, '%Y-%m-%d')
        #           end_date = datetime.strptime(end_date, '%Y-%m-%d')
        num_days = (end_date - start_date).days

        # Multiply the number of days with the vehicle price
        price = vehicle.vehicles_price * num_days

        return JsonResponse({'price': price})
