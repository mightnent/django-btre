from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        print("post")
        listing_id = request.POST['listing_id']
        listing = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email'] 

        #check if user has already made an inquiry on the same listing
        if request.user.is_authenticated:
            #user_id = request.user_id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"A prior inquiry has been made")
                return redirect('/listings/'+listing_id)



        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        send_mail(
            'Property listing inquiry',
            'There has been an inquiry on '+listing+'. You can log into admin panel to check it out.',
            'xxx@gmail.com',
            [realtor_email,"xxx@gmail.com"],
            fail_silently=False
        )

        messages.success(request,"Submitted!")

        return redirect('/listings/'+listing_id)