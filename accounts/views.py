from django.shortcuts import render
from django.views.generic import View, TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

class UserRegitrationView(View):
    model = User
    template_name='accounts/user_register.html'
    form_class =UserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class AboutAuthorView(TemplateView):
    template_name ='accounts/about.html'

