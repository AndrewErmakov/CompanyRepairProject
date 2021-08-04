from django.contrib.auth import logout


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


