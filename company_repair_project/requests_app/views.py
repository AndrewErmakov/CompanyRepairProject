from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.views import View

from clients_app.models import Client
from requests_app.forms import NewRequestForm


class CreateRequestView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewRequestForm()
        return render(request, 'new_request.html', {'form': form})

    def post(self, request):
        form = NewRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.customer = Client.objects.get(user=request.user)
            new_request.save()

            return redirect('chat_request')
        else:
            return render(request, 'create_request.html', {'form': form})
