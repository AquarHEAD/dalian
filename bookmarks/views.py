from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from dalian.bookmarks.models import Category, Bookmark

# this function add the visited count of a bookmark and redirect to it
def goto(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    bookmark.visited += 1
    bookmark.save()
    return redirect(bookmark.url)

# the following 3 functions are used in control hub's main page
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

# the bookmark manage page
def manage(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        categories = Category.objects.all()
        for category in categories:
            category.bookmarks = []
            for bookmark in category.bookmark_set.all():
                category.bookmarks.append(bookmark)
        return render_to_response('bookmarks/manage.html', {'categories': categories}, context_instance=RequestContext(request))
    else:
        return redirect('/login')

# the bookmark edit page
def edit_bookmark(request, bookmark_id):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
        if request.method == 'POST':
            bookmark.save(name = request.POST['name'], url = request.POST['url'], category = Category.objects.get(pk=request.POST['category']))
            if request.POST.get('archive', default = False):
                bookmark.archive = True
                bookmark.save()
        else:
            categories = Category.objects.all()
            return render_to_response('bookmarks/edit_bookmark.html', {'bookmark': bookmark, 'categories': categories}, context_instance=RequestContext(request))
    else:
        return redirect('/login')
