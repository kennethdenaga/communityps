from django.shortcuts import render, redirect
from django.http import HttpResponse
from kenlist.models import Donator, Donation, Recipient, Location, Remarks

#community pantry




def home_page(request):
    donators = Donator.objects.all()
    return render(request, 'homepage.html', {'donators':donators})

def homepage(request):
    donators = Donator.objects.all()
    return render(request, 'homepage.html', {'homepage':homepage})

def signup(request):
    donators = Donator.objects.all()
    return render(request, 'signup.html', {'signup':signup})

def donator(request):
    donators = Donator.objects.all()
    return render(request, 'donator.html', {'donators':donators})

def donation(request):
    donators = Donator.objects.all()
    return render(request, 'donation.html', {'donation':donation})

def recepient(request):
    donators = Donator.objects.all()
    return render(request, 'recepient.html', {'recepient':recepient})

def profile(request):
    donators = Donator.objects.all()
    return render(request, 'profile.html', {'profile':profile})

def about(request):
    donators = Donator.objects.all()
    return render(request, 'about.html', {'about':about})

def info(request):
    donators = Donator.objects.all()
    return render(request, 'info.html', {'info':info})

def contact(request):
    donators = Donator.objects.all()
    return render(request, 'contact.html', {'contact':contact})

def view_donator(request, donator_id):
    donator_ = Donator.objects.get(id=donator_id)
    return render(request, 'donation.html', {'donator': donator_})

  
def new_donator(request):
    donator_ = Donator.objects.create()
    #donator_ = Donator.objects.create(name=request.POST['name'],contactnumber=request.POST['contact'], donator = donator_)
    return redirect(f'/kenlist/{donator_.id}/')

def add_donation(request, donator_id):
    donator_ = Donator.objects.get(id=donator_id)
    #donation.objects.create(donation_type=request.POST['typedonation'], donation=request.POST['donation'],donator_)
    return redirect(f'/kenlist/{donator_id}/')


def datamanipulation(request):
    #Creating teacher's data
    donator = Donator(name="Kenneth", contactnumber="09054990958" )
    donator.save()

    #Read all data
    donator = Donator.objects.all()
    result = 'Printing all Donation : <br>'
    for x in teacher:
        res += X.adviser+"<br>"

    #Read one data
    donator =  Donator.get(contactnumber="09054990958")
    res += "Printing one teacher profile : <br>"
    res += ddonator.address


    res+= '<br> Deletinng... <br>'
    ddonator.delete()

    #Update/Creating data
    donators = Donator(name="Kenneth", contactnumber="09167005138" )
    donators.save()
    res += 'Updating...<br>'

    donators = Donator.objects.get(name="Kenneth")
    donators.contactnumber= "09167005138"
    donators.save()
    res = ""

    #Filtering data
    qs = Donation.objects.filter(donation="Fruits")
    res += "found : %s result<br>"%len(qs)

    #ordering data
    qs = Donator.objects.order_by("name")
    for x in qs: 
        res += x.contactnumber + '<br>'








