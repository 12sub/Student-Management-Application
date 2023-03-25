from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from app.models import UserAgent
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agents_list.html"
    
    def get_queryset(self):
        return UserAgent.objects.all()
    
class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agents")

