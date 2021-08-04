from django.contrib.auth import logout

from clients_app.models import Client


class ClientManager:

    def create_client(self, user_form, client_info_form):
        account = user_form.save()

        client = client_info_form.save(commit=False)
        client.user = account
        client.save()

    def delete_client(self, request):
        authorized_user = request.user
        logout(request)
        authorized_user.delete()

    def update_client(self, request, authorized_user):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        authorized_user.username = username
        authorized_user.first_name = first_name
        authorized_user.last_name = last_name

        authorized_user.save()

        client = Client.objects.get(user=authorized_user)
        client.phone_number = phone_number
        client.address = address
        client.save()
