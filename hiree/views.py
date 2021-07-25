from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import HireeInfo,HireeSkills
from django.contrib import messages
from django.contrib.auth.decorators import login_required


import os


# Create your views here.
def signup(request):
    if request.method=="POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('hiree:info')


        else:
            messages.error(request, 'Please Enter Unique Username and Password')
            print(form.error_messages)



        return render(request, 'hiree/accounts.html', {'form': form})


    else:
        return render(request,'hiree/accounts.html')

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('hiree:profile')
        else:
            messages.error(request,'Please check Your details once again')
            print(form.errors)


        return render(request, 'hiree/accounts.html', context={'form': form})
    else:
        return render(request, 'hiree/accounts.html')




@login_required(login_url="/hiree/signin/")
def info(request):
    if request.method=="POST":
        full_name=request.POST.get('hiree_name')
        ph_numb = request.POST.get('hiree_number')

        img=request.FILES.get('img',False)
        area = request.POST.get('hiree_area')
        city= request.POST.get('hiree_city')
        pincode = request.POST.get('hiree_pincode')
        gender = request.POST.get('gender')




        infoOb=HireeInfo(full_name=full_name,Phone_numb=ph_numb,profile_pic=img,Area=area,City=city,pincode=pincode,gender=gender)

        infoOb.person = request.user
        infoOb.save()

        return redirect('hiree:skills')




    return render(request,'hiree/info.html')



@login_required(login_url="/hiree/signin/")
def skills(request):
    if request.method=="POST":
        skill=request.POST.get('hiree_skills')
        exp = request.POST.get('hiree_exp')
        charge = request.POST.get('hiree_charge')
        Area = request.POST.get('hiree_AvalArea')
        time = request.POST.get('hiree_AvalTime')
        others = request.POST.get('hiree_others')

        skillob=HireeSkills(hiree_skills=skill,hiree_exp=exp,hiree_charge=charge,hiree_AvalArea=Area,hiree_AvalTime=time,hiree_other=others)
        skillob.person = request.user
        skillob.save()

        return redirect('hiree:thankyou')
    return render(request,'hiree/skills.html')


@login_required(login_url="/hiree/signin/")
def profile(request):
    p1=request.user
    print(p1)
    skills = HireeSkills.objects.all()
    info = HireeInfo.objects.all()

    ans=[]
    image=""
    for ob in info:
        if ob.person==p1:

            image=ob.profile_pic.url
            ans.append(ob)

            break
    print(ans)
    for ob2 in skills:
        if ob2.person==p1:
            ans.append(ob2)
            break
    print(ans)

    return render(request, 'hiree/profile.html', {'person': ans[0],'skill':ans[1],'img':image,'user':p1})




@login_required(login_url="/hiree/signin/")
def thankyou(request):
    return render(request,'hiree/thank.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')


