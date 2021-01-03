from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,state_choices,bedroom_choices
from .models import Single_Listing

# Create your views here.
def index(request):
    Listings = Single_Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(Listings,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Listings' : page_obj,
    }
    return render(request,'listings/listings.html',context)

#listing_id comes from urls.py of listing
def single_listing(request,listing_id):
    listing = get_object_or_404(Single_Listing,pk=listing_id)
   
    context = {
        'listing':listing,
    }
    return render(request,'listings/single_listing.html',context)

def search(request):
    queryset_list = Single_Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        #check if empty string
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    if 'state' in request.GET:
        state = request.GET['state']
        #check if empty string
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        #check if empty string
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        #check if empty string
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    context = {
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'Listings' : queryset_list,
        'values': request.GET
    }
    return render(request,'listings/search.html',context)
