from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from random import choice
from dalian.notes.models import Note
from dalian.settings import LOGIN_KEY

def manage(request):
    notes = Note.objects.all()
    