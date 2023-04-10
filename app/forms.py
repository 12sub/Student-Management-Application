from django import forms
from django.contrib.auth import get_user_model
from .models import Management, Lecturers, Students, User, UserAgent
from django.contrib.auth.forms import UserCreationForm, UsernameField

# User = get_user_model()

class AppModelForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = (
            'name',
            'email',
            'profession',
            'date_of_employment',
            'organization'
        )
        
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = (
            'name',
            'email',
            'Lecturers',
            'year_level',
            'academic_level',
            'description'
        )
class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {'username': UsernameField}
    
class AppForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    profession = forms.CharField()
    date_of_employment = forms.DateField()
    
class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=UserAgent.objects.none())
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        print(request.user)
        agents = UserAgent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset =  agents