# myapp/middleware.py

from django.shortcuts import redirect
from django.conf import settings

class SinglePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('authenticated'):
            if request.path != settings.PASSWORD_LOGIN_URL and request.method != 'POST':
                return redirect(settings.PASSWORD_LOGIN_URL)
        response = self.get_response(request)
        return response
