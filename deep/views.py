from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Person
from django.core.exceptions import PermissionDenied


def detail(request, person_id):
    try:
        p = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return HttpResponse(p.full_name)


def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def permission_denied_view(request):
    raise PermissionDenied

