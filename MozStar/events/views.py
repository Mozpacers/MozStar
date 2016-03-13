from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Event
from .serializers import EventSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def event_list(request):
    """
    List all Events, or create a new Event.
    """
    if request.method == 'GET':
        event = Event.objects.filter(is_published=True)
        serializer = EventSerializer(event, many=True)
        return JSONResponse(serializer.data)

    '''
    Currently just read-only API

    Un-comment the following code to allow creating events
    '''

    '''
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    '''


@csrf_exempt
def event_detail(request, pk):
    """
    Retrieve, update or delete a Event.
    """
    try:
        event = Event.objects.get(eid=pk, is_published=True)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JSONResponse(serializer.data)

    '''
    Currently just read-only API

    Un-comment the following code to allow updating and deleting events
    '''

    '''
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Event.delete()
        return HttpResponse(status=204)
    '''

