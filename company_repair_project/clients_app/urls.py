from django.urls import path
from clients_app.views import LoginClientView, RegistrationView
urlpatterns = [
    path('login/', LoginClientView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),

]
