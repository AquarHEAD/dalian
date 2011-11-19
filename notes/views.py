from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from dalian.notes.models import Note
from dalian.utils.decorators import login_check
from dalian.settings import LOGIN_KEY

@login_check(LOGIN_KEY)
def manage(request):
    notes = Note.objects.all().order_by('-stat_date')
    paginator = Paginator(notes, 13)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        show_notes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        show_notes = paginator.page(paginator.num_pages)
    
    return render_to_response('notes/manage.html', {'notes': show_notes}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def add(request):
    if request.method == 'POST':
        new_note = Note.objects.create(content = request.POST['content'])
    return redirect('/ctrlhub/main')

@login_check(LOGIN_KEY)
def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.content = request.POST['content']
        note.save()
        return redirect('/notes/manage')
    else:
        return render_to_response('notes/edit.html', {'note': note}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def remove(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('/notes/manage')