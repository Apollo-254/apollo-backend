"""
Function for displaying error 404 and 500 views
"""

from django.http import JsonResponse
from utils.messages.hundle_messages import errorResponse


def error_404(request, exception):
    message = 'The endpoint not found. Check your spelling or add a trailing slash </> at the end of the endpoint.'
    data = errorResponse(status_code=404, error_code='Not_Found', message=message)
    response = JsonResponse(data=data, )
    response.status_code = 404
    return response


def error_500(request):
    message = "Server experienced an internal error that needs technical attention"
    data = errorResponse(status_code=500, error_code='Internal server error', message=message)

    response = JsonResponse(data=data, )
    response.status_code = 500
    return response
