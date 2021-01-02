from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Single_Listing

# Create your views here.
def index(request):
    Listings = Single_Listing.objects.order_by(-'list_date').filter(is_published=True)
    paginator = Paginator(Listings,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Listings' : page_obj
    }
    return render(request,'listings/listings.html',context)

#listing_id comes from urls.py of listing
def single_listing(request,listing_id):
    return render(request,'listings/single_listing.html')

def search(request):
    return render(request,'listings/search.html')
