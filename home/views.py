from django.shortcuts import render , redirect
from django.http import HttpResponse
from home.utils import send_email_to_client, send_email_with_attachment

from django.conf import settings
from .models import *
import random

# from home.utils import *

# Create your views here.

def home(request):
#     return HttpResponse('''
# <h1>Hey I am a Django Server.</h1>
# <p>Hey This is coming from Django Server</p>
# <hr>
# <h3>Hope You are loving it.:)</h3>                     
# ''')

    # Car.objects.create(
    #     car_name=f"Nexon-{random.randint(0,100)}"
    # )

    peoples=[
        {'Name':'Abhijeet Gupta','Age':26},
        {'Name':'Rohan Sharma','Age':23},
        {'Name':'Vicky Kaushal','Age':17},
        {'Name':'Deepanshu Chaurasiya','Age':16},
        {'Name':'Sandeep Choudhary','Age':63},
    ]




    vegetables=['Pumpkin','Tomato','Potato']


    return render(request, 'home/index.html', context={'page':'Django 2024 Tutorial Page','peoples': peoples, 'vegetables':vegetables})


def contact(request):
    context={'page':'Contact'}
    return render(request,"home/contact.html",context)


def about(request):
    context={'page':'About Us'}
    return render(request,"home/about.html",context)

def send_email(request):
    # send_email_to_client()
    file_path=f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachment("This is a test message.","Hello How Are You? Hey Please Find this attached file with this email",['abhisek.rinku2000@gmail.com'],'main.xlsx')


    return redirect('/')

