from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from leads.models import Lead
from properties.models import Property
@login_required
def dashboard_home(request):
    total_leads = Lead.objects.count()
    total_properties = Property.objects.count()

    context = {
        'total_leads': total_leads,
        'total_properties': total_properties,
    }

    return render(request, 'dashboard/home.html', context)
