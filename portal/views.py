from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.views.generic.base import View

from portal.forms import addApplicationForm
from portal.models import Application, Message, Service


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
        print(self.request.META)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        context['object_list'] = self.get_queryset().filter(ip=ip)
        return context


class OthersView(TemplateView):
    template_name = 'other.html'


class SelectServiceView(ListView):
    template_name = 'chooseService.html'
    model = Service


class AddApplicationView(CreateView):
    template_name = 'addApplication.html'
    form_class = addApplicationForm
    success_url = reverse_lazy('applications')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        form.fields['service_detail'].queryset = Service.objects.get(name=self.kwargs['name']).service_detail.all()
        context['form'] = form
        return context

    def form_valid(self, form, **kwargs):
        """If the form is valid, save the associated model."""
        form_save = form.save(commit=False)
        form_save.service = Service.objects.get(name=self.kwargs['name'])
        form_save.state = 'Зарегистрировано'
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




