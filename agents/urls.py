from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agents"),
    path('create/', AgentCreateView.as_view(), name='agents_create'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agents_detail'),
    path('<int:pk>/update', AgentUpdateView.as_view(), name='agents_update'),
    path('<int:pk>/delete', AgentDeleteView.as_view(), name='agents_delete'),
]