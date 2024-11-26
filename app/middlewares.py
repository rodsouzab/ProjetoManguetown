
from django.urls import reverse
from django.shortcuts import redirect

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != reverse('manguetown:login'):
            return redirect('manguetown:login')
        return self.get_response(request)