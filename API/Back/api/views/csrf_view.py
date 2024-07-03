from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(View):
    """View class for setting CSRF token as a cookie."""

    def get(self, request, *args, **kwargs):
        """Handle GET requests for setting CSRF token."""
        return JsonResponse({'success': 'CSRF cookie set'})
