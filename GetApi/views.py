from django.http import JsonResponse
from .models import GetApi
from .serializers import GetApiSerializer
import json
from django.shortcuts import render

#from django.http import 
from GetApi import views

def get_api(request):

    #get all details
    #serialize them
    #retrn json

#    getApi = GetApi.objects.all()
 #   serializer = GetApiSerializer(getApi, many=True)

    #return (JsonResponse(serializer.data, safe=False))
    #return {slackUsername: 'Saviour Eking'}
    #return json.dumps(get_api)

    return JsonResponse({"slackUsername": "Saviour Eking", "backend": True, "age": 20, "bio": "I am a backend developer inter at HNG"})

    #{"slackUsername": "Saviour Eking", "backend": true, "age": 20, "bio": "I am a backend developer inter at HNG"}]