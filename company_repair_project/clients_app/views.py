from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from clients_app.business import ClientManager
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
        user_form = ExtendedAccountCreationForm(request.POST)
        client_info_form = AdditionalClientInfoForm(request.POST)

        if user_form.is_valid() and client_info_form.is_valid():
            ClientManager().create_client(user_form, client_info_form)
            return redirect('login')

        else:
            return render(request, 'new_client.html', {'form': user_form, 'client_info_form': client_info_form})


class DeleteClientAccountView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')

    def post(self, request):
        ClientManager().delete_client(request)
        return redirect('login')


class UpdateClientAccountView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        authorized_user = request.user
        return render(request, 'update_account.html', {'user': authorized_user})

    def post(self, request):
        authorized_user = request.user
        ClientManager().update_client(request, authorized_user)

        return redirect('list_requests')


