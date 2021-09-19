from django.shortcuts import render
from Admin_app import models
from student.models import Application
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
# Create your views here.
class SuperUserMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
class Home(TemplateView):
    template_name='eapp/base.html'
class Pending(SuperUserMixin,ListView):
    template_name ='eapp/pending.html'
    model=models.Requests
    context_object_name='list'
    def get_queryset(self):
        qs=super(Pending,self).get_queryset()
        return qs.filter(status__exact='pending')
class Confirmed(SuperUserMixin,ListView):
    template_name ='eapp/confirmed.html'
    model=models.Requests
    context_object_name='list'
    def get_queryset(self):

        qs=super(Confirmed,self).get_queryset()
        return qs.filter(status__exact='confirmed')
class Rejected(SuperUserMixin,ListView):
    template_name ='eapp/rejected.html'
    model=models.Requests
    context_object_name='list'
    def get_queryset(self):
        qs=super(Rejected,self).get_queryset()
        return qs.filter(status__exact='rejected')

def ViewDetail(request,pk):
    if request.user.is_superuser:
        qs = models.Requests.objects.get(id=pk)
        if request.method =='POST':
            message = request.POST.get('message')
            qs.status='rejected'
            qs.save()

            rej = models.Rejected.objects.create(message=message,req=qs)
            rej.save()
            return render(request,'eapp/base.html')
        else:
            return render(request,'eapp/detail.html',{'list':qs})
    else: pass


def Registration(request,pk):
    if request.user.is_superuser:
        if request.method=='POST':
            code = request.POST.get('reg')
            qs = models.Accepted.objects.filter(Registration_Number=code)
            dis =False
            if qs :
                dis=True
            else:
                dis=False
                contact = models.Requests.objects.get(req_no=pk)
                contact.status='confirmed'
                contact.save()

                qs = models.Accepted.objects.create(user=contact.req_no.user,Registration_Number=code)
                qs.save()
                return render(request,'eapp/base.html')
            return render(request,'eapp/accept.html',{'dis':dis})

        else:
            return render(request,'eapp/accept.html',{'dis':False})
    else: pass

def Rejected_detail(request,pk):

    qs = models.Rejected.objects.get(id=pk)
    return render(request,'eapp/reject.html',{'list':qs})
