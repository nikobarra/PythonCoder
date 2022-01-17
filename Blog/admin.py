from django.contrib import admin

# Register your models here.

from .models import Post, Profile, Relationship

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Relationship)