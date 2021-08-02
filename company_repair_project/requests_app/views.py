from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import UpdateView

from clients_app.models import Client
from requests_app.additional_modules.get_date_separator import get_date_separator
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

        status_list = request.GET.getlist('status', [])

        if status_list:
            status_filters = Q(status=status_list[0])

            for i in range(1, len(status_list)):
                status_filters |= Q(status=status_list[i])

            requests = requests.filter(status_filters)

        request_type = request.GET.get('type', '')
        if request_type:
            requests = requests.filter(type=request_type)

        date = request.GET.get('date', '')
        if date:
            date_separator = get_date_separator(date)
            parsed_date = date.split(date_separator)
            requests = requests.filter(creation_date__year=parsed_date[-1],
                                       creation_date__month=parsed_date[1],
                                       creation_date__day=parsed_date[0]
                                       )

        return render(request, 'list_requests.html', {'requests': requests})


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = Request
    template_name = 'request_update.html'
    fields = ['type', 'title', 'description', 'status']
    success_url = reverse_lazy('list_requests')


class DeleteRequestView(LoginRequiredMixin, View):
    def post(self, request, pk):
        chosen_request = Request.objects.get(pk=pk)
        chosen_request.delete()
        return redirect('list_requests')
