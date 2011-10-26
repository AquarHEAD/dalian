from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from dalian.settings import ADMIN_PASSWORD
from dalian.bookmarks.models import Category

def login(request):
    if request.method == 'POST':
        if request.POST['password'] == ADMIN_PASSWORD:
            request.session['sudo'] = 'dalian'
            return redirect('/ctrlhub')
        else:
            return redirect('/login')
    else:
        return render_to_response('ctrlhub/login.html', {}, context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['sudo']
    except KeyError:
        pass
    return redirect('/')

def ctrl_main(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        categories = Category.objects.all()
        return render_to_response('ctrlhub/main.html', {'categories': categories}, context_instance=RequestContext(request))
    else:
        return redirect('/login')