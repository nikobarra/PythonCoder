from django.shortcuts import render


def home(request):
    
    return render(request, 'FinalApp/home.html')

def about(request):
    
    return render(request, 'FinalApp/about.html')





