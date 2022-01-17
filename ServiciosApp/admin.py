from django.contrib import admin

# Register your models here.
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Services, ServicesAdmin)
