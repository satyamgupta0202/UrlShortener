import json
from time import time
from warnings import catch_warnings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import shorten
from .models import shortUrl
import time
from .serializers import shortUrlSerializer
from django.core import exceptions
from .Awssqs import poll
from .dynamoDb import put_item,get_item
# Create your views here.
Url = "http://127.0.0.1:8000/api/createShorten/"
from . import shorten


@api_view(['POST'])
def createShorten(req):
    body = json.loads(req.body)
    counter = poll()
    try:
        short_url = f"{Url}{shorten.encode_base62(int(counter['Messages'][0]['Body']))}"
        # shortend = shortUrl.objects.create(shortUrl = short_url , longUrl = body['url'])
        # shortend.save()
        item = put_item(short_url, body['url'], counter['Messages'][0]['Body'])
        print(item)
        return Response({
            'shortUrl':short_url,
            'longUrl':body['url']
        })
    except:
        print(counter,type(counter))
        return Response("There is some problem in post request")

@api_view(['Get'])
def redirectUrl(req,id):
    try:
        # long_url = shortUrlSerializer(shortUrl.objects.get(shortUrl = Url+id)).data['longUrl']
        shortUrl = Url+id
        long_Url = get_item(shortUrl)
       
        return redirect(long_Url['Item']['longUrl'])
        
    except exceptions.ObjectDoesNotExist:
        return HttpResponse("Short Url Des not Exist")