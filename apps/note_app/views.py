from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import NoteForm



# Create your views here. 
def index(request): 
    allNotes = Note.objects.all()
    noteF = NoteForm
    context = {

        'all_notes' : allNotes,
        'noteForm' : noteF,

    }

    return render(request, 'note_app/index.html', context) 



def register(request):
    noteF = NoteForm(request.POST)
    if noteF.is_valid():
        note = Note.objects.create(content=request.POST['content'])
        note.save()
    else:
        print('invalid note')


    return redirect('/notes/')

