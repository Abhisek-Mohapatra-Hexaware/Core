from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import *

from .seed import generate_report_card

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
@login_required(login_url= "/login/")
def recipes(request):


    if request.method=="POST":
        data = request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")


        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect("/recipes/")

    queryset=Recipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context={'page':'Recipe Page','recipes':queryset}
    return render(request,"recipes.html",context)


def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=data.get('recipe_image')


        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if recipe_image:
            queryset.recipe_image=recipe_image

        queryset.save()
        return redirect('/recipes/')

    context={'recipe':queryset}
    return render(request,'update_recipe.html',context)

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')


        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists!")
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )


        user.set_password(password)
        user.save()

        messages.info(request,'Account Created Successfully!')
        return redirect('/register/')


    context={'page':'Register Page'}
    return render(request,'register.html',context)


def login_page(request):
    context={'page':'Login Page'}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/login/')

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')



    return render(request,'login.html',context)


from django.db.models import Q

def get_students(request):
    queryset=Student.objects.all()

    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('marks','-student_age')

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_id__student_id__icontains=search) |
            Q(department__department__icontains=search) |
            Q(student_name__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search)
        )



    paginator = Paginator(queryset, 25)

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)


    context={'page':'Get Students Page','queryset':page_obj}

    return render(request,'report/students.html',context)

def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)



    context={'page':'See Student Marks','queryset':queryset}
    return render(request,'report/see-marks.html',context)









