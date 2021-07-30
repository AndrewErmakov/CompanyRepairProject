from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.views import View

from clients_app.models import Client
from requests_app.forms import NewRequestForm
from requests_app.models import Request


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

            return redirect('list_requests')
        else:
            return render(request, 'create_request.html', {'form': form})


class ListRequestsView(LoginRequiredMixin, View):
    def get(self, request):
        requests = Request.objects.all()
        return render(request, 'list_requests.html', {'requests': requests})


class RequestDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        chosen_request = Request.objects.get(pk=pk)
        return render(request, 'request_detail.html', {'request': chosen_request})


class DeleteRequestView(LoginRequiredMixin, View):
    def post(self, request, pk):
        chosen_request = Request.objects.get(pk=pk)
        chosen_request.delete()
        return redirect('list_requests')
