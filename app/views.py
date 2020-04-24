from uuid import uuid4

from django.http import response

from .tasks import a_task


def repro(request):
    a_task.send(
        {
            'value': str(uuid4()),
        },
    )
    return response.HttpResponse()
