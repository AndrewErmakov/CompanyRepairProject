from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from requests_app.business import ManagerRequests, create_request
from requests_app.forms import NewRequestForm
from requests_app.models import Request


class CreateRequestView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = NewRequestForm()
        return render(request, 'new_request.html', {'form': form})

    def post(self, request):
        form = NewRequestForm(request.POST)
        if form.is_valid():
            create_request(form, request.user)
            return redirect('list_requests')
        else:
            return render(request, 'create_request.html', {'form': form})


class ListRequestsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        requests_manager = ManagerRequests(params=dict(request.GET), current_user=request.user)

        # depending on user role get requests
        requests = requests_manager.get_requests_depending_on_user_role()

        if requests_manager.filter_flag:
            requests = requests_manager.get_filtered_requests()

        return render(request, 'list_requests.html', {'requests': requests})


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Request
    template_name = 'request_update.html'
    fields = ['type', 'title', 'description', 'status']
    success_url = reverse_lazy('list_requests')


class DeleteRequestView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Request
    success_url = reverse_lazy('list_requests')
