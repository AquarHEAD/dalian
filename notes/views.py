from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.encoding import smart_str, smart_unicode
from dalian.notes.models import Note
from dalian.utils.decorators import login_check
from dalian.settings import LOGIN_KEY
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import misaka

@login_check(LOGIN_KEY)
def home(request):
    notes = Note.objects.all()
    return render_to_response('notes/home.html', {'notes': notes}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def add(request):
    if request.method == 'POST':
        new_note = Note.objects.create(name=request.POST['name'], content=request.POST['content'], lang=request.POST['lang'], password=request.POST['password'])
        if request.POST.get('private', default = False):
            new_note.private = True
        new_note.save()
    return redirect('/notes/home')

@login_check(LOGIN_KEY)
def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.name = request.POST['name']
        note.content = request.POST['content']
        note.lang = request.POST['lang']
        note.password = request.POST['password']
        if request.POST.get('private', default = False):
            note.private = True
        note.save()
        return redirect('/notes/home')
    else:
        return render_to_response('notes/edit.html', {'note': note}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def remove(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('/notes/home')

def view(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if note.lang:
        note.is_code = True
        lexer = get_lexer_by_name(note.lang, stripall=True)
        formatter = HtmlFormatter(linenos=True, cssclass="note-content")
        note.result = highlight(note.content, lexer, formatter)
    else:
        note.is_code = False
        note.result = misaka.html(smart_str(note.content))
    sudo = request.session.get('sudo', default = None)
    if sudo == LOGIN_KEY:
        notes = Note.objects.all()
        return render_to_response('notes/show.html', {'viewing_note': note, 'notes': notes}, context_instance=RequestContext(request))
    else:
        if show_note.private:
            return redirect('/ctrlhub/login')
        else:
            return render_to_response('notes/show_pub.html', {'styles': styles, 'viewing_note': note}, context_instance=RequestContext(request))
