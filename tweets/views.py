from django.http import HttpResponse, Http404, JsonResponse

from django.shortcuts import render
from .models import Tweet


# Create your views here.

def home(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """

    :param request:
    :param tweet_id:
    :param args:
    :param kwargs:
    :return:

    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data

    """
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f'<h1>Hello {tweet_id} - {obj.content}</h1>')
