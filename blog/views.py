from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def starting_page(request):
    return HttpResponse()


def posts(request):
    pass


def post_detail(request, slug):
    pass
