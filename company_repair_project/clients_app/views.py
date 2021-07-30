from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from clients_app.forms import ExtendedAccountCreationForm, AdditionalClientInfoForm


class LoginClientView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'


class RegistrationView(View):
    def get(self, request):
        form = ExtendedAccountCreationForm()
        client_info_form = AdditionalClientInfoForm()
        return render(request, 'new_client.html', {'form': form, 'client_info_form': client_info_form})

    def post(self, request):
        form = ExtendedAccountCreationForm(request.POST)
        client_info_form = AdditionalClientInfoForm(request.POST)

        if form.is_valid() and client_info_form.is_valid():
            account = form.save()

            client = client_info_form.save(commit=False)
            client.user = account
            client.save()

            return redirect('login')

        else:
            return render(request, 'new_client.html', {'form': form, 'client_info_form': client_info_form})
