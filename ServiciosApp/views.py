from django.shortcuts import render
from ServiciosApp.models import Services
# Create your views here.
def services (request):
    services = Services.objects.all()
    
    return render(request, 'ServiciosApp/services.html', {"services":services})