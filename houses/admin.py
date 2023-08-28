from django.contrib import admin

# Register your models here.
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    list_display = ("name", "price_per_night", "description", "address", "pets_allowed")
    list_filter = ("price_per_night", "pets_allowed")
    search_fields = ("name", "address")