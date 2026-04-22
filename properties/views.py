from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm

def property_list(request):
    properties = Property.objects.all()

    search = request.GET.get('search')
    property_type = request.GET.get('property_type')

    if search:
        properties = properties.filter(location__icontains=search)

    if property_type:
        properties = properties.filter(property_type=property_type)

    return render(request, 'properties/property_list.html', {'properties': properties})


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)   # ✅ change here
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()

    return render(request, 'properties/add_property.html', {'form': form})


def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)   # ✅ change here
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)

    return render(request, 'properties/add_property.html', {'form': form})


def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')

    return render(request, 'properties/delete_property.html', {'property': property})