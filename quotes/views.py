from django.shortcuts import redirect
from django.template import RequestContext
from dalian.quotes.models import Quote

def add(request):
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        if request.method == 'POST':
            new_quote = Quote.objects.create(content = request.POST['content'])
        return redirect('/ctrlhub/main')
    else:
        return redirect('/ctrlhub/login')