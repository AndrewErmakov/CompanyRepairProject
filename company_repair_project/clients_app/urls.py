from django.urls import path
from clients_app.views import LoginClientView, RegistrationView, DeleteClientAccountView

urlpatterns = [
    path('login/', LoginClientView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('delete_client', DeleteClientAccountView.as_view(), name='delete_client'),
]
