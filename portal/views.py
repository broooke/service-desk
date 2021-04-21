from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.views.generic.base import View

from portal.forms import addApplicationForm
from portal.models import Application, Message


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ApplicationsView(ListView):
    template_name = 'applications.html'
    model = Application

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        context['object_list'] = self.get_queryset().filter(ip=ip)
        return context

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


class SignInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('applications')
    redirect_authenticated_user = True


class LogOutView(LogoutView):
    next_page = reverse_lazy('login')


class AdminPanelView(ListView):
    template_name = 'adminPanel.html'
    model = Application


class DoneApplicationView(View):
    def post(self, request, pk):
        application = Application.objects.get(id=pk)
        application.state = 'Выполнено'
        application.save()
        return redirect('admin-panel')


class ApplicationDetailView(DetailView):
    template_name = 'applicationDetail.html'
    model = Application
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=self.get_object().id)
        context['room_name'] = self.get_object().id
        context['username'] = self.request.user.first_name if self.request.user.is_staff else self.get_object().user
        return context




