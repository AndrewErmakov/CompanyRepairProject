from django.db.models import Q

from clients_app.models import Client
from requests_app.additional_modules.get_date_separator import get_date_separator
from requests_app.additional_modules.get_random_executor import get_random_executor
from requests_app.models import Request


class ManagerRequests:
    def __init__(self, params, current_user):
        self.requests = Request.objects.all()
        self.params = params
        self.filter_flag = bool(params)
        self.current_user = current_user



    def get_requests_depending_on_user_role(self):
        if not self.current_user.client.is_worker:
            self.requests = self.requests.filter(customer__user=self.current_user)

        else:
            self.requests = self.requests.filter(executor__user=self.current_user)

        return self.requests

    def filter_by_statuses(self, status_list):
        status_filters = Q(status=status_list[0])

        for i in range(1, len(status_list)):
            status_filters |= Q(status=status_list[i])

        return self.requests.filter(status_filters)

    def filter_by_specific_date(self, date):
        date_separator = get_date_separator(date)
        parsed_date = date.split(date_separator)
        return self.requests.filter(creation_at__year=parsed_date[-1],
                                    creation_at__month=parsed_date[1],
                                    creation_at__day=parsed_date[0]
                                    )

    def filter_by_date_range(self, first_date, second_date):
        return self.requests.filter(creation_at__date__range=[first_date, second_date])

    def filter_by_request_type(self, request_type):
        return self.requests.filter(type=request_type)

    def get_filtered_requests(self):
        if self.params.get('status'):
            self.requests = self.filter_by_statuses(self.params['status'])

        if self.params.get('type'):
            self.requests = self.filter_by_request_type(self.params['type'][0])

        if self.params.get('first_date') and self.params.get('second_date'):
            self.requests = self.filter_by_date_range(self.params['first_date'][0], self.params['second_date'][0])

        if self.params.get('date'):
            self.requests = self.filter_by_specific_date(self.params['date'][0])

        return self.requests


def create_request(form, current_user):
    new_request = form.save(commit=False)

    new_request.customer = Client.objects.get(user=current_user)
    new_request.executor = Client.objects.get(pk=get_random_executor()).user

    new_request.save()
