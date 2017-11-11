from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import UserNotes

# Create your views here.

def home(request):
    notes = UserNotes.objects
    #template = loader.get_template('notes_view.html')
    context = {'notes': notes}
    return render(request, 'notes_view.html', context)
    #return render_to_response("notes_view.html", notes)

