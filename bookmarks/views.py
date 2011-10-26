from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from dalian.bookmarks.models import Category, Bookmark

def goto(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    bookmark.visited += 1
    bookmark.save()
    return redirect(bookmark.url)
    
def create_category(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        if request.method == 'POST':
            new_cat = Category.objects.create(name = request.POST['name'])
        return redirect('/ctrlhub')
    else:
        return redirect('/login')
        
def add_bookmark(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        if request.method == 'POST':
            new_bookmark = Bookmark.objects.create(name = request.POST['name'], url = request.POST['url'], category = Category.objects.get(pk=request.POST['category']))
            if request.POST.get('archive', default = False):
                new_bookmark.archive = True
                new_bookmark.save()
        return redirect('/ctrlhub')
    else:
        return redirect('/login')

def add_with_cat(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        if request.method == 'POST':
            new_cat = Category.objects.create(name = request.POST['category'])
            new_bookmark = Bookmark.objects.create(name = request.POST['name'], url = request.POST['url'], category = new_cat)
            if request.POST.get('archive', default = False):
                new_bookmark.archive = True
                new_bookmark.save()
        return redirect('/ctrlhub')
    else:
        return redirect('/login')

def manage(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        categories = Category.objects.all()
        return render_to_response('bookmarks/manage.html', {'categories': categories}, context_instance=RequestContext(request))
    else:
        return redirect('/login')