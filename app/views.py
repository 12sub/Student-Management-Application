from django.shortcuts import render, redirect, reverse 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import User, Management, Lecturers, Students
from .forms import AppForm, AppModelForm, AssignAgentForm, StudentModelForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from agents.mixins import OrganisorAndLoginRequiredMixin

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserForm
    
    def get_success_url(self):
        return reverse("login")

def landing_page(request):
    return render(request, 'landing.html')

@login_required
def home_page(request):
    model = Management.objects.all()
    context = {
        'user': model
    }
    return render(request, 'index.html', context=context)

@login_required
def students_page(request):
    model = Students.objects.all()
    context = {
        'user': model
    }
    return render(request, 'students.html', context=context)

class ManagementListView(LoginRequiredMixin, ListView):
    template_name = 'app_list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        queryset = Students.objects.all()
        if self.request.user.is_agent:
            queryset = queryset.filter(agent_user=self.request.user)
        return queryset
    


@login_required
def app_detail(request, pk):
    model = Management.objects.get(id=pk)
    context = {
        'students': model
    }
    return render(request, 'app_list.html', context=context)

class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'app_student_list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Management.objects.filter(organization=user.userprofile)
        else:
            queryset = Management.objects.filter(organization=user.useragent.organization)
            #Filter for agent logged in
            queryset = queryset.filter(agent_user=user)
        return queryset
    # def get_context_data(self, **kwargs):
        # user = self.request.user
    #     context = super(ManagementListView, self).get_context_data(**kwargs)
    #     if user.is_organisor:
    #         queryset = Management.objects.filter(
    #             organization=user.userprofile, 
    #             agent__isnull = True)
    #     context.update({
    #         "unassigned_leads": queryset
    #     })

@login_required
def app_student_detail(request, pk):
    model = Students.objects.get(id=pk)
    context = {
        'students': model
    }
    return render(request, 'app_student_list.html', context=context)

# class ManageCreateView(CreateView):
#     template_name = 'app_create.html'
#     form_class = AppModelForm
    
#     def get_success_url(self):
#         return reverse('app_detail')
#     def form_valid(self, form):
#         send_mail(
#             subject="A management has been created",
#             message="Go to site to see new management",
#             from_email="test@test.com",
#             recipient_list=["test2@test.com"]
#         )
#         return super(ManageCreateView, self).form_valid(form)
    
@login_required
def app_create(request):
    form = AppModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = AppModelForm(request.POST)
        if form.is_valid():
            send_mail(
            subject="A management has been created",
            message="Go to site to see new management",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
            print("The form is valid")
            # print(form.cleaned_data)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            profession = form.cleaned_data['profession']
            date_of_employment = form.cleaned_data['date_of_employment']
            organization = form.cleaned_data['organization']
            # lecturers = Lecturers.objects.first()
            Management.objects.create(
                name=name,
                email=email,
                profession=profession,
                date_of_employment=date_of_employment, 
                organization=organization
            )
            print('Lead Has been created!!!')
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'app_create.html', context=context)

@login_required
def app_students(request):
    form = StudentModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            print('Student Has been created!!!')
            return redirect('/app/student1')
    context = {
        'form': form
    }
    return render(request, 'app_students.html', context=context)

@login_required
def app_students_update(request, pk):
    model = model = Students.objects.get(id=pk)
    form = StudentModelForm(instance=model)
    if request.method == "POST":
        print("Receiving a post request")
        form = StudentModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            print('Student Has been successfully updated!!!')
            return redirect('/app/student1')
    context = {
        'form': form,
        'model':model
    }
    return render(request, 'app_students_update.html', context=context)

@login_required
def app_update(request, pk):
     model = Management.objects.get(id=pk)
     form = AppModelForm(instance=model)
     if request.method == "POST":
        print("Receiving a post request")
        form = AppModelForm(request.POST, instance=model)
        if form.is_valid():
            print("The form is valid")
            model.save()
            print('Management Has been updated!!!')
            return redirect('/')
     context = {
         'form': form,
        'user': model
    }
     return render(request, 'app_update.html', context=context)

@login_required
def app_delete(request, pk):
    model = Management.objects.get(id=pk)
    model.delete()
    return redirect('/')

@login_required
def app_student_delete(request, pk):
    model = Students.objects.get(id=pk)
    model.delete()
    return redirect('/')

class AssignAgentView(OrganisorAndLoginRequiredMixin, FormView):
    template_name = "assign_agent.html"
    form_class = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs
        kwargs.update({
            "request": self.request
        })
        return kwargs
        
    def get_success_url(self):
        return reverse('app_detail')
    
    def form_valid(self, form):
        agent =form.cleaned_data["agent"]
        app = Management.objects.get(id=self.kwargs["pk"])
        app.agent = agent
        app.save()
        return super(AssignAgentView, self).form_valid(form)