from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.method== 'POST':
        username = request.POST['name']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME ALREADY EXISTS")
                return redirect('register')

            elif User.objects.filter(password=password).exists():
                    messages.info(request, "PASSWORD ALREADY EXISTS")
                    return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.info(request, "USER CREATED")
                return redirect('login')
        else:
            messages.info(request, "PASSWORD NOT MATCHED")
            return redirect('register')
    return render(request,'register.html' )
def page(request):
    return render(request,'header.html')

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password3 = request.POST.get('pass')
        user=auth.authenticate(username=user,password=password3)
        if user is not None:
            auth.login( request, user)

            return render(request,'header.html')
        else:
            return redirect('login')

    return render(request,'sign.html')

def logout(request):
    auth.logout(request)
    return redirect('page')

def person(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "APPLICATION PROCESSED")
            return redirect('person')
    return render(request, 'home.html',{'form': form} )
def home(request):
    return render(request,'home1.html')
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html',{'form': form} )


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)