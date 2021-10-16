from django.http import HttpResponse
from .models import Note
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Note, pk=question_id)
    return render(request, 'note/results.html', {'Note': Note})
