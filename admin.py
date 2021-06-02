from django.contrib import admin
from .models import Post
from .models import City

# Register your models here.

admin.site.register(Post)
admin.site.register(City)