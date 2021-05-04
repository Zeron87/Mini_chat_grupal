from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from users.models import User

from django.views.generic import (
    TemplateView
)

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:user-login')
    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


