from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, \
    UpdateView, DeleteView, DetailView
# alternatively ... from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.
class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads/leads-all.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "leads/lead-detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/lead-create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadUpdateView(UpdateView):
    template_name = "leads/lead-update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name = "leads/lead-delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
