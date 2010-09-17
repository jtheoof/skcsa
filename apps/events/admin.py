from django.contrib import admin
from models import Address

class AddressAdmin(admin.ModelAdmin):
    fields = ('name', 'street', 'zipcode', 'city', 'country')
    
admin.site.register(Address, AddressAdmin)
