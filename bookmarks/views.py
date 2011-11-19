from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from dalian.bookmarks.models import Bookmark
from dalian.categories.models import Category
from dalian.utils.decorators import login_check
from dalian.settings import LOGIN_KEY

# this function add the visited count of a bookmark and redirect to it
def goto(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    bookmark.visited += 1
    bookmark.save()
    return redirect(bookmark.url)

# the following 2 functions are used in control hub's main page
@login_check(LOGIN_KEY)
def add(request):
    if request.method == 'POST':
        new_bookmark = Bookmark.objects.create(name = request.POST['name'], url = request.POST['url'], category = Category.objects.get(pk=request.POST['category']))
        if request.POST.get('archive', default = False):
            new_bookmark.archive = True
            new_bookmark.save()
    return redirect('/ctrlhub/main')

@login_check(LOGIN_KEY)
def add_with_cat(request):
    if request.method == 'POST':
        new_cat = Category.objects.create(name = request.POST['category'])
        new_bookmark = Bookmark.objects.create(name = request.POST['name'], url = request.POST['url'], category = new_cat)
        if request.POST.get('archive', default = False):
            new_bookmark.archive = True
        new_bookmark.save()
    return redirect('/ctrlhub/main')

# the bookmark manage page
@login_check(LOGIN_KEY)
def manage(request):
    categories = Category.objects.all()
    for category in categories:
        category.bookmarks = []
        for bookmark in category.bookmark_set.all():
            category.bookmarks.append(bookmark)
    return render_to_response('bookmarks/manage.html', {'categories': categories}, context_instance=RequestContext(request))

# the bookmark edit page
@login_check(LOGIN_KEY)
def edit(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    if request.method == 'POST':
        bookmark.name = request.POST['name']
        bookmark.url = request.POST['url']
        bookmark.category = Category.objects.get(pk=request.POST['category'])
        if request.POST.get('archive', default = False):
            bookmark.archive = True
        else:
            bookmark.archive = False
        bookmark.save()
        return redirect('/bookmarks/manage')
    else:
        categories = Category.objects.all()
        return render_to_response('bookmarks/edit.html', {'bookmark': bookmark, 'categories': categories}, context_instance=RequestContext(request))

# removing the bookmark
@login_check(LOGIN_KEY)
def remove(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    bookmark.delete()
    return redirect('/bookmarks/manage')
