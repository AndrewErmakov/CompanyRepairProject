from django.urls import path
from requests_app.views import CreateRequestView, ListRequestsView, RequestDetailView, DeleteRequestView

urlpatterns = [
    path('create_request/', CreateRequestView.as_view(), name='create_request'),
    path('list_requests/', ListRequestsView.as_view(), name='list_requests'),
    path('request_detail/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('delete_request/<int:pk>/', DeleteRequestView.as_view(), name='delete_request'),
]
