from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lead, Client
from .forms import LeadForm, ClientForm


# ──────────── Dashboard ────────────

@login_required(login_url='/login/')
def crm_dashboard(request):
    context = {
        'segment': 'crm_dashboard',
        'total_leads': Lead.objects.count(),
        'total_clients': Client.objects.count(),
        'new_leads': Lead.objects.filter(status='New').count(),
        'converted_leads': Lead.objects.filter(status='Converted').count(),
        'recent_leads': Lead.objects.all()[:5],
        'recent_clients': Client.objects.all()[:5],
    }
    return render(request, 'crm/dashboard.html', context)


# ──────────── Lead CRUD ────────────

@login_required(login_url='/login/')
def lead_list(request):
    leads = Lead.objects.all()
    context = {'segment': 'leads', 'leads': leads}
    return render(request, 'crm/lead_list.html', context)


@login_required(login_url='/login/')
def lead_add(request):
    form = LeadForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Lead added successfully.')
        return redirect('lead_list')
    context = {'segment': 'leads', 'form': form, 'title': 'Add Lead'}
    return render(request, 'crm/lead_form.html', context)


@login_required(login_url='/login/')
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Lead updated successfully.')
        return redirect('lead_list')
    context = {'segment': 'leads', 'form': form, 'title': 'Edit Lead', 'lead': lead}
    return render(request, 'crm/lead_form.html', context)


@login_required(login_url='/login/')
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted.')
        return redirect('lead_list')
    context = {'segment': 'leads', 'lead': lead}
    return render(request, 'crm/lead_confirm_delete.html', context)


# ──────────── Client CRUD ────────────

@login_required(login_url='/login/')
def client_list(request):
    clients = Client.objects.all()
    context = {'segment': 'clients', 'clients': clients}
    return render(request, 'crm/client_list.html', context)


@login_required(login_url='/login/')
def client_add(request):
    form = ClientForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Client added successfully.')
        return redirect('client_list')
    context = {'segment': 'clients', 'form': form, 'title': 'Add Client'}
    return render(request, 'crm/client_form.html', context)


@login_required(login_url='/login/')
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Client updated successfully.')
        return redirect('client_list')
    context = {'segment': 'clients', 'form': form, 'title': 'Edit Client', 'client': client}
    return render(request, 'crm/client_form.html', context)


@login_required(login_url='/login/')
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted.')
        return redirect('client_list')
    context = {'segment': 'clients', 'client': client}
    return render(request, 'crm/client_confirm_delete.html', context)
