from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(['GET', 'POST'])
def update_profile_page(request):
    response = HttpResponse()
    return response
