from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    #id is built in
    list_display = ('id','name','listing','email','contact_date')
    list_display_link = ('id','name')
    search_fields = ('name','email','listing')

admin.site.register(Contact,ContactAdmin)
