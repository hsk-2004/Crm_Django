from django.urls import path
from . import views

urlpatterns = [
    # CRM Dashboard
    path('crm/', views.crm_dashboard, name='crm_dashboard'),

    # Leads
    path('crm/leads/', views.lead_list, name='lead_list'),
    path('crm/leads/add/', views.lead_add, name='lead_add'),
    path('crm/leads/<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('crm/leads/<int:pk>/delete/', views.lead_delete, name='lead_delete'),

    # Clients
    path('crm/clients/', views.client_list, name='client_list'),
    path('crm/clients/add/', views.client_add, name='client_add'),
    path('crm/clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('crm/clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
]
