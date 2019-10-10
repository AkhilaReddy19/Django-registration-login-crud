from django.shortcuts import render, redirect, HttpResponse
from .models import Profile,City
from register.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic.edit import UpdateView

# Create your views here.
def registration(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            print(request.POST)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            city = request.POST.get('city')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            tandc = request.POST.get('tandc')

            Profile.objects.create(first_name=first_name,last_name=last_name,gender=gender,email=email,phone=phone,city=city,password=password,confirm_password=confirm_password,tandc=tandc)
            messages.success(request, "You have registered successfully!")
            return render(request,'success.html')
        else:
            print(form.errors)
            return render(request, 'registration.html',{'form':form})

    form = ProfileForm()
    cities = City.objects.all()
    context = {'form':form,'cities':cities}
    return render(request,'registration.html',context)

def success(request):
    return render(request, 'login.html')


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not(Profile.objects.filter(email=email).exists()):
            messages.error(request, "Enter valid email id or password")
            return render(request, 'login.html')

        if(Profile.objects.filter(email=email).exists()):
            details = Profile.objects.get(email=email)
            user_id = Profile.objects.get(email=email).id
            user_password = Profile.objects.get(pk=user_id).password
            if(user_password == password):
                user = authenticate(email=email, password=password)
                login(request, user)
                return render(request,'home.html',{'details':details})
            else:
                messages.error(request, "Enter valid email id or password")
                return render(request, 'login.html')


# def Login(request):
#     user=authenticate(
#         email=request.POST['email'],
#         password=request.POST['password']
#     )
#     if user is not None:
#         login(request,user)
#         return render(request, 'home.html')
#     else:
#         messages.error(request,"Enter valid email id or password")
#         return render(request, 'login.html')

def home(request, id):
    details = Profile.objects.get(pk=id)
    return render(request, 'home.html', {'details': details})

def edit(request, id):
    details = Profile.objects.get(pk=id)
    cities = City.objects.all()
    context = {'details': details, 'cities': cities}
    return render(request,'edit.html',context)

def update(request, id):
    details = Profile.objects.get(pk=id)
    form = ProfileForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            details.first_name = request.POST.get('first_name')
            details.last_name = request.POST.get('last_name')
            details.city = request.POST.get('city')
            details.save()
            return render(request, 'home.html',{'details':details})
        else:
            return render(request, 'edit.html',{'details':details})
    else:
        return render(request, 'edit.html', {'details': details})

def view_profile(request,id):
    details = Profile.objects.get(pk=id)
    return render(request, "display.html", {'details': details})



# class update(UpdateView):
#     model = Profile
#     fields = ['first_name','last_name','city']

# def update(request, id):
#     details = Profile.objects.get(pk=id)
#     form = ProfileForm(request.POST, instance=details)
#     messages.info(request,form)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             messages.info(request,"in")
#             return render(request, 'home.html',{'details': details})
#         else:
#             messages.info(request, "out")
#             return render(request, 'edit.html', {'form': form})
