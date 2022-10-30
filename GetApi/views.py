from django.http import JsonResponse
from .models import GetApi
from .serializers import GetApiSerializer

def get_api(request):

    #get all details
    #serialize them
    #retrn json

    getApi = GetApi.objects.all()
    serializer = GetApiSerializer(getApi, many=True)

    return (JsonResponse(serializer.data, safe=False))