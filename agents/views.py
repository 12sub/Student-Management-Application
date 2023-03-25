from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        return UserAgent.objects.all()
    
    
class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agents_update.html'
    context_object_name = 'agent'
    form_class = AgentModelForm
    
    def get_queryset(self):
        return UserAgent.objects.all()
    
    def get_success_url(self):
        return reverse("agents:agents")
    
class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'agents/agents_delete.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        return UserAgent.objects.all()
    
    def get_success_url(self):
        return reverse("agents:agents")


