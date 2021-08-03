import random

from clients_app.models import Client


def get_random_executor():
    workers = Client.objects.filter(is_worker=True)
    random_worker = random.choice(workers)
    return random_worker.id

