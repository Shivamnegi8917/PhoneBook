from django.contrib import admin

# Register your models here.
from .models import PhoneBook

admin.site.register(PhoneBook)