from django.shortcuts import render
from django.views.generic import View


class AccountView(View):
    template_name = "account/account.html"

    def get(self, request):
        return render(request, self.template_name)
