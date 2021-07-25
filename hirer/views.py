from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import Data
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.apps import apps
hireeInfo = apps.get_model('hiree', 'HireeInfo')
hireeskill = apps.get_model('hiree', 'HireeSkills')



# Create your views here.
# def signup(request):
#     if request.method=="POST":
#         form = UserCreationForm(data=request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#
#             return redirect('hirer:search')
#
#
#         else:
#             messages.error(request, 'Please Enter Unique Username and Password')
#
#         return render(request, 'hirer/signup.html', {'form': form})
#
#
#     else:
#         return render(request,'hirer/signup.html')

# def signin(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request,user)
#             return redirect('hirer:search')
#
#
#         else:
#             messages.error(request, 'Please check Your details once again')
#
#             return render(request, 'hirer/signup.html', {'form': form})
#
#     else:
#         return render(request, 'hirer/signup.html')
#
#
#     return render(request, 'hirer/signup.html',{'form': form})


def search(request):
    if request.method=="POST":
        global occu
        global place
        occu = request.POST.get('occupation')
        place = request.POST.get('place')

        return redirect('hirer:employees')

    return render(request, 'hirer/hirer_search.html')

def employees(request):

    skills = hireeskill.objects.all()
    pers=[ p for p in skills if p.hiree_skills.lower()== occu.lower() ]

    list=hireeInfo.objects.all()
    l=[]
    for p in pers:
        for ob in list:
            if ob.person == p.person and ob.City.lower() == place.lower():
                name=ob.full_name
                numb=ob.Phone_numb
                pic=ob.profile_pic.url

                City=ob.City
                skills=p.hiree_skills
                exp=p.hiree_exp
                charge=p.hiree_charge
                ob1=Data(full_name=name,Phone_numb=numb,profile_pic=pic,City=City,skills=skills,exp=exp,charge=charge)
                l.append(ob1)

    if l:
        return render(request,'hirer/search_res.html',{'list':l})
    else:
        return render(request, 'hirer/no_res.html')


