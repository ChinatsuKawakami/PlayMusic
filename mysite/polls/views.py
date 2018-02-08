
from django.http import HttpResponse

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

def index(request):
    return HttpResponse('Hello world');
# Create your views here.
