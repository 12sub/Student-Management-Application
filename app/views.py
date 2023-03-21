from django.shortcuts import render, redirect, reverse 
from django.core.mail import send_mail
from .models import User, Management, Lecturers, Students
from .forms import AppForm, AppModelForm, StudentModelForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView
from django.db import IntegrityError

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserForm
    
    def get_success_url(self):
        return reverse("login")

def landing_page(request):
    return render(request, 'landing.html')

def home_page(request):
    model = Management.objects.all()
    context = {
        'user': model
    }
    return render(request, 'index.html', context=context)

def students_page(request):
    model = Students.objects.all()
    context = {
        'user': model
    }
    return render(request, 'students.html', context=context)

def app_detail(request, pk):
    model = Management.objects.get(id=pk)
    context = {
        'students': model
    }
    return render(request, 'app_list.html', context=context)

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
            # lecturers = Lecturers.objects.first()
            Management.objects.create(
                name=name,
                email=email,
                profession=profession,
                date_of_employment=date_of_employment
            )
            print('Lead Has been created!!!')
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'app_create.html', context=context)

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

def app_delete(request, pk):
    model = Management.objects.get(id=pk)
    model.delete()
    return redirect('/')

def app_student_delete(request, pk):
    model = Students.objects.get(id=pk)
    model.delete()
    return redirect('/')