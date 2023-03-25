from django import forms
from app.models import UserAgent

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = UserAgent
        fields = (
            'user',
        )