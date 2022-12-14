from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings


from . import forms


class SignUpView(View):
    template_name = "authentication/signup.html"
    form_class = forms.SignUpForm

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={"form": form})
