from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from dalian.settings import ADMIN_PASSWORD, LOGIN_KEY
from dalian.categories.models import Category
from dalian.utils.decorators import login_check

def login(request):
    if request.method == 'POST':
        if request.POST['password'] == ADMIN_PASSWORD:
            request.session['sudo'] = LOGIN_KEY
            return redirect('/ctrlhub/main')
        else:
            return redirect('/ctrlhub/login')
    else:
        return render_to_response('ctrlhub/login.html', {}, context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['sudo']
    except KeyError:
        pass
    return redirect('/')

@login_check(LOGIN_KEY)
def ctrl_main(request):
    categories = Category.objects.all()
    return render_to_response('ctrlhub/main.html', {'categories': categories}, context_instance=RequestContext(request))