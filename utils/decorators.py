from django.shortcuts import redirect
from functools import wraps

def login_check(key):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):  
            sudo = request.session.get('sudo', default = None)
            if sudo == key:
                return func(request, *args, **kwargs)
            else:
                return redirect('/ctrlhub/login')
        return wraps(func)(inner_decorator)
    return decorator