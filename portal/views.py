from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from portal.forms import addApplicationForm
from portal.models import Application


class ApplicationsView(ListView):
    template_name = 'applications.html'
    model = Application

class OthersView(TemplateView):
    template_name = 'other.html'


class AddApplicationView(CreateView):
    template_name = 'addApplication.html'
    form_class = addApplicationForm
    success_url = reverse_lazy('applications')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form_save = form.save(commit=False)
        form_save.state = 'Зарегистрировано'
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            form_save.ip = x_forwarded_for.split(',')[0]
        else:
            form_save.ip = self.request.META.get('REMOTE_ADDR')
        form_save.save()
        return super().form_valid(form)

