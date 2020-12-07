from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view(request, *args, **kwargs)
    return wrapper


def allow_to_view(allowed_roles=[]):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view(request, *args, **kwargs)
            else:
                return HttpResponse('You have not enough rights to view this page')
        return wrapper
    return decorator

def admin_only(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return view(request, *args, **kwargs)
        else:
            return redirect('store:products')
    return wrapper