from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from dalian.categories.models import Category
from dalian.utils.decorators import login_check
from dalian.settings import LOGIN_KEY

@login_check(LOGIN_KEY)
def manage(request):
    categories = Category.objects.all()
    return render_to_response('categories/manage.html', {'categories': categories}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def add(request):
    if request.method == 'POST':
        new_cat = Category.objects.create(name = request.POST['name'])
    return redirect('/ctrlhub/main')

@login_check(LOGIN_KEY)
def rename(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('/categories/manage')
    else:
        return render_to_response('categories/rename.html', {'category': category}, context_instance=RequestContext(request))
        
@login_check(LOGIN_KEY)
def remove(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('/categories/manage')