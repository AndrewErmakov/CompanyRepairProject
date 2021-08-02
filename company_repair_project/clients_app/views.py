from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from clients_app.forms import ExtendedAccountCreationForm, AdditionalClientInfoForm
from clients_app.models import Client


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


class DeleteClientAccountView(LoginRequiredMixin, View):
    def post(self, request):
        authorized_user = request.user
        logout(request)
        authorized_user.delete()
        return redirect('login')


class UpdateClientAccountView(LoginRequiredMixin, View):
    def get(self, request):
        authorized_user = request.user
        return render(request, 'update_account.html', {'user': authorized_user})

    def post(self, request):
        authorized_user = request.user

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        authorized_user.username = username
        authorized_user.first_name = first_name
        authorized_user.last_name = last_name

        authorized_user.save()

        client = Client.objects.get(user=authorized_user)
        client.phone_number = phone_number
        client.address = address
        client.save()

        return redirect('list_requests')
