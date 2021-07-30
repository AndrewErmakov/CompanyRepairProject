from django.urls import path
from requests_app.views import CreateRequestView
urlpatterns = [
    path('create_request/', CreateRequestView.as_view(), name='create_request'),
]
