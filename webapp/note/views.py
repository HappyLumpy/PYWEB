from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'note/results.html')


class Notelist(APIView):
    def get(self, request):
        notes = Note.objects.filter(public=True)
        res = []
        for note in notes:
            res.append({
                'id': note.id,
                'title': note.title,
                'author': {
                    'id': note.author.id,
                    'username': note.author.username,
                }
            })

        return Response(res)

    def post(self, request):
        pass


class BlogViewMix(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
