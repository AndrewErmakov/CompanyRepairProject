from django.shortcuts import render

from django.views import View


class CreateRequestView(View):
    def get(self, request):
        return render(request, 'new_request.html')
