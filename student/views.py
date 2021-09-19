from django.shortcuts import render,HttpResponse,redirect
from student.models import Application
from django.contrib import messages
from django.contrib.auth.models import User
from Admin_app import models
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
import json
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def application(request):
        if request.user.is_authenticated:
            vis = True
            qs = models.Requests.objects.filter(user=request.user,status='pending')
            qs2 = models.Requests.objects.filter(user=request.user,status='confirmed')
            if qs or qs2:
                vis=False
                msg=''
                code =''
                if qs2:
                    msg='Your Request has been accepted, Your registraton Number is -'
                    code = models.Accepted.objects.get(user=request.user)
                else:
                    msg='Your request is still pending wait'
                return render(request,'home/application.html',{"vis":vis,"code":code,"msg":msg})

            username = request.user.username
            user=username

        #details=Application.objects.filter(user=request.user)
        #print(details)

        COMPUTER_SCIENCE = 'Computer Science'
        ELECTRICAL = 'Electrical'

        CS_1 = 'DSA'
        CS_2 = 'Big Data'
        CS_3 = 'Machine Learning'
        EE_1 = 'Controllers'
        EE_2 = 'MicroControllers'
        EE_3 = 'Miniprocessors'

        SUBJECT_CHOICES =[COMPUTER_SCIENCE,ELECTRICAL]

        cs_strings = [CS_1,CS_2,CS_3]
        b_strings = [EE_1,EE_2,EE_3]

        json_cs_strings = json.dumps(cs_strings)
        json_b_strings = json.dumps(b_strings)

        context={}
        context['json_cs_strings'] = json_cs_strings
        context['json_b_strings'] = json_b_strings
        context['subjects']=SUBJECT_CHOICES


        if request.method=='POST':
            name=request.POST['name']
            birthdate=request.POST['birthdate']
            aadhar=request.POST['aadhar']
            address=request.POST['address']
            gender=request.POST['gender']
            department=request.POST['department']
            specialization=request.POST['specialization']
            category=request.POST['category']
            pwd=request.POST['pwd']
            documents=request.FILES.get('documents', None)
            photo=request.FILES.get('photo', None)
            notes=request.POST['notes']

            if len(name)<2:
                messages.error(request,"Length of name should be greater than 2. Please fill the form correctly")
            elif len(aadhar)!=12:
                messages.error(request,"Incorrect aadhar number. Please fill the form correctly")
            # elif file_extension != '.pdf':
            #     messages.error(request,"wrong document format")
            else:
                messages.success(request, "Form submitted successfully.")
            #print(name,aadhar,notes)
            submitted='yes'
            application=Application(name=name,birthdate=birthdate,aadhar=aadhar,address=address,gender=gender,
            department=department,specialization=specialization,category=category,documents=documents,photo=photo,submitted=submitted,
            user=request.user,notes=notes,pwd=pwd)
            application.save()
            context['vis']=False
            req = models.Requests.objects.create(user=request.user,req_no=application)
            req.save()
        return render(request, 'home/application.html', context)

def handleSignup(request):
    if request.method == 'POST':
        print('yes')
        #Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #checks
        if len(username)>10:
            messages.error(request, 'Your Username must be less than 10 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, 'Your Username must be alnum')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        if  User.objects.filter(username=username).exists():
            messages.error(request, 'This Username is not available')
            return redirect('home')

        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'Your account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home')
    return HttpResponse('404 - Not Found')

class Reject_list(LoginRequiredMixin,ListView):
    template_name='home/reject_list.html'
    context_object_name='list'
    model=models.Requests
    def get_queryset(self):
        qs=super(Reject_list,self).get_queryset()
        return qs.filter(status__exact='rejected')


def handleLogout(request):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('home')

def Rejected_detail(request,pk):

    qs = models.Rejected.objects.get(id=pk)
    return render(request,'home/reject.html',{'list':qs})
