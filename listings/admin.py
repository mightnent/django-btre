from django.contrib import admin

# Register your models here.
from .models import Single_Listing

class Listing_Admin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','zipcode','price','address','realtor__name')  
    list_per_page = 25 
admin.site.register(Single_Listing,Listing_Admin)