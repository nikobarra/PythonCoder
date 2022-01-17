from django.urls import path
from FinalApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', views.home, name="Home"),
    path ('about', views.about , name="About"),
    
    
        
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)