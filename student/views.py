from django.shortcuts import render,HttpResponse,redirect
from student.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"please fill the form correctly")
        else:
            messages.success(request, "Form submitted successfully")
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request, 'home/contact.html')

def handleSignup(request):
    if request.method == 'POST':
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

def handleLogout(request):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('home')
