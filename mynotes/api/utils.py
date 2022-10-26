from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@csrf_exempt
def createNote(request):
    # data = request.data
    data = JSONParser().parse(request)
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@csrf_exempt
def updateNote(request, pk):
    data = JSONParser().parse(request)
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data

@csrf_exempt
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')