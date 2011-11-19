from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from dalian.tweets.models import Tweet
from dalian.utils.decorators import login_check
from dalian.settings import LOGIN_KEY

@login_check(LOGIN_KEY)
def manage(request):
    tweets = Tweet.objects.all().order_by('-stat_date')
    paginator = Paginator(tweets, 13)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        show_tweets = paginator.page(page)
    except (EmptyPage, InvalidPage):
        show_tweets = paginator.page(paginator.num_pages)
    
    return render_to_response('tweets/manage.html', {'tweets': show_tweets}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def add(request):
    if request.method == 'POST':
        new_tweet = Tweet.objects.create(content = request.POST['content'])
    return redirect('/ctrlhub/main')

@login_check(LOGIN_KEY)
def edit(request, tweet_id):
    t = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == 'POST':
        t.content = request.POST['content']
        t.save()
        return redirect('/tweets/manage')
    else:
        return render_to_response('tweets/edit.html', {'tweet': t}, context_instance=RequestContext(request))

@login_check(LOGIN_KEY)
def remove(request, tweet_id):
    t = get_object_or_404(Tweet, pk=tweet_id)
    t.delete()
    return redirect('/tweets/manage')