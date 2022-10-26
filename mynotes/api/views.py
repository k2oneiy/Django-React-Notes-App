from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Note
from .serializers import NoteSerializer

from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote


# Create your views here.


@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# @api_view(['GET'])
# def getNotes(response):
#     notes = Note.objects.all().order_by('-updated')
#     serializers = NoteSerializer(notes,many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def getNote(response,pk):
#     notes = Note.objects.get(id=pk)
#     serializers = NoteSerializer(notes,many=False)
#     return Response(serializers.data)    

# @api_view(['GET', 'PUT', 'DELETE'])    
# def updateNote(request,pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializers = NoteSerializer(instance=note,data=data)
#     if serializers.is_valid():
#         serializers.save()
#     return serializers.data

# @api_view(['DELETE'])    
# def deleteNote(request,pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted')


@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)




