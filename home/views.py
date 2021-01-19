from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from  .models import skills,Project,Contact
from django.http import HttpResponse,HttpResponseRedirect
from .models import skills,Project
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
import json
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.
def home (request):
    return render(request,'home/index.html')

def about(request):


    #allprods = []
    #catprods = Product.objects.values('category', 'id')
    #cats = {item['category'] for item in catprods}
    #params = {'allprods': allprods}
    return render(request,'home/about.html')

def skill(request):
    ski= skills.objects.all()
    context = {'ski': ski}
    return render(request,'home/skill.html',context)

def project(request):
    pro = Project.objects.all()
    cont = {'pro': pro}
    return render(request,'home/project.html',cont)

def proj(request):
    pro = Project.objects.all()
    cont = {'pro': pro}
    return render(request,'home/proj.html',cont)

def other(request):
    return render(request,'home/other.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        msg = request.POST.get('msg', '')
        print(fname, lname,email, msg)
        contact = Contact(fname=fname,lname=lname, email=email,  msg=msg)
        contact.save()
        thank = True
    return render(request, 'home/contact.html', {'thank': thank})


def register(request):
    # if this is a POST request we need to process the form data
    template = 'home/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                #login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/home/index.html')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})