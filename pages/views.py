from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,state_choices,bedroom_choices
from listings.models import Single_Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    Listings = Single_Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'Listings':Listings,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices  
    }
    return render(request,'pages/index.html',context)

def about(request):
    Realtors = Realtor.objects.order_by('-hire_date')
    MVP = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'Realtors' : Realtors,
        'MVP' : MVP
    }
    return render(request,'pages/about.html',context)
