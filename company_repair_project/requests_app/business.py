from django.db.models import Q

from requests_app.additional_modules.get_date_separator import get_date_separator


class ManagerRequests:
    def __init__(self, requests, params):
        self.requests = requests
        self.params = params
        self.filter_flag = bool(params)

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


