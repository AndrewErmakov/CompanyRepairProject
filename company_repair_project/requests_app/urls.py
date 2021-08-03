from django.urls import path
from requests_app.views import CreateRequestView, ListRequestsView, RequestUpdateView, DeleteRequestView

urlpatterns = [
    path('create_request/', CreateRequestView.as_view(), name='create_request'),
    path('list_requests/', ListRequestsView.as_view(), name='list_requests'),
    path('update_request/<int:pk>/', RequestUpdateView.as_view(), name='update_request'),
    path('delete_request/<int:pk>/', DeleteRequestView.as_view(), name='delete_request'),
]