from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from . models import *
from django.http import HttpResponse
from .decorators import *
from django.db.models import Q

@role_based
def index(request):
    return render(request, 'ipdc/index.html')
def investor_dashboard(request):
    unseen_notifications=Notification.objects.filter(user=request.user)
    not_count=len(unseen_notifications)
    context={'unseen_notifications':unseen_notifications,'not_count':not_count}
    return render(request, 'ipdc/Investor_dashboard/investor_personal_information.html',context)

def investor_project_information(request):
    return render(request, 'ipdc/Investor_dashboard/investor_project_information.html')

def investor_file_information(request):
    return render(request, 'ipdc/Investor_dashboard/investor_file_information.html')

def park_admin_dashboard(request):
    return render(request, 'ipdc/Park_admin_dashboard/index3.html')

def manager_dashboard(request):
    return render(request, 'ipdc/manager_dashboard/index2.html')

def board_dashboard(request):
    return render(request, 'ipdc/Board_dashboard/index2.html')

def oiib_dashboard(request):
    return render(request, 'ipdc/OIIB_Dashboard/index4.html')

#New content added
def investor_profile(request):
    return render(request, 'ipdc/Investor_dashboard/investor_profile.html')

def live_camera(request):
    return render(request, 'ipdc/Investor_dashboard/live_camera.html')

def license_request(request):
    return render(request, 'ipdc/Investor_dashboard/license_request.html')

def all_investor(request):
    return render(request, 'ipdc/Park_admin_dashboard/all_investor.html')

def view_investor_profile(request):
    return render(request, 'ipdc/Park_admin_dashboard/view_investor_profile.html')

def proposal(request):
    return render(request, 'ipdc/Park_admin_dashboard/proposal.html')

def pdfviewer(request):
    return render(request, 'ipdc/Park_admin_dashboard/pdf_viewer.html')


@login_required(login_url='login')
def investorprofilepage(request):
    try:
        investor=Investor.objects.get(user=request.user)
    except:
        investor=Investor.objects.filter(user=request.user).first

    investorform=InvestorForm()
    unseen_notifications=Notification.objects.filter(user=request.user)
    not_count=len(unseen_notifications)
    if request.method =="POST":
        print("and again")
        if investor:
            print("pre")
            investorform=InvestorForm(request.POST,request.FILES,instance=investor)
            print("working ...")
        else:
            investorform=InvestorForm(request.POST,request.FILES)
        if investorform.is_valid():
            investor=investorform.save(commit=False)
            investor.user = request.user
            investor.save()

            return HttpResponse('added')
    context={'investor':investor,'un_seen_notifications':unseen_notifications,'not_count':not_count}
    return render(request, 'ipdc/Investor_dashboard/investor_profile.html',context)

@login_required(login_url='login')
def request_land(request):
    try:
        landrequested=DomesticRequest.objects.get(investor=request.user.investor)
    except:
        landrequested=DomesticRequest.objects.filter(investor=request.user.investors).first

    landform=LandForm()
    
    if request.method =='POST':
        if landrequested:
            landform=LandForm(request.POST , request.FILES,instance=landrequested)
        else:
            landform=LandForm(request.POST , request.FILES)
        if landform.is_valid():
            land=landform.save(commit=False)
            invest=Investor.objects.get(user=request.user)
            land.investor = invest
            land.save()
            return HttpResponse("done")
    context={'landform':landform,'land_requested':landrequested}
    return render(request, 'ipdc/Investor_dashboard/investor_file_information.html',context)

@login_required(login_url='login')
def chat(request,pk):
    privatechats=Privatechat.objects.filter(Q(primary_user=request.user) | Q(secondary_user=request.user))
    privateroom=Privatechat.objects.get(id=pk)
    messages=Message.objects.filter(privatechat=privateroom)
    if privateroom.primary_user.username == request.user.username:
        friend=privateroom.secondary_user
    else:
        friend=privateroom.primary_user
    messageform=MessageForm()
    if request.method == 'POST':
        messageform=MessageForm(request.POST,request.FILES)
        if messageform.is_valid():
            messagefor=messageform.save(commit=False)
            messagefor.privatechat=privateroom
            messagefor.written_by=request.user
            messagefor.save()    
    context={'privatechats':privatechats,'friend':friend,'messages':messages,'privatechat':pk}
    return render(request, 'ipdc/Investor_dashboard/chat.html',context)

@login_required(login_url='login')
def chatpage(request):
    privatechats=Privatechat.objects.filter(Q(primary_user=request.user) | Q(secondary_user=request.user))
    
    context={'privatechats':privatechats}
    return render(request, 'ipdc/Investor_dashboard/chatt.html',context)



@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        print("working")
        email = request.POST.get('email')
        password =request.POST.get('password')
        try:
            user = authenticate(request, username=email, password=password)
        except:
            return HttpResponse('INvalid uer or pass')
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'ipdc/login.html', context)





def logoutpage(request):
    logout(request)
    return redirect('login')


