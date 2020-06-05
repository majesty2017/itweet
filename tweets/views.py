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
    data = {
        "id": tweet_id,
        # "image_path": obj.image.url
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        data['message'] = 'Not Found'
        status = 404

    return JsonResponse(data, status=status)
