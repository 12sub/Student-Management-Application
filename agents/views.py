from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import UserAgent

class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agents_list.html"
    
    def get_queryset(self):
        return UserAgent.objects.all()

