from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print(request.POST)
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        listing =  request.POST['listing']
        name =  request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already requested for this listing!')
                return redirect('listing', listing_id=listing_id)

        contact = Contact(listing=listing, listing_id = listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # SEND EMAIL BUT PLESAE PUT YOUR EMAIL IN realstate setting.py
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for'+ listing + ' by ' + name + ' Sign into the admin panel for more.'
        #     'youremail@email.com',
        #     ['receiver1@gmail.com', email],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been recorded, our realtor will soon contact you')
        return redirect('listing', listing_id=listing_id)
    return 
