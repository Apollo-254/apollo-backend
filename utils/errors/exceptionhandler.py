from rest_framework.views import exception_handler
from utils.messages.hundle_messages import errorResponse


def customExceptionHandler(exc, context):
    handlers = {
        'ValidationError': _handle_request_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'UnsupportedMediaType': _handle_generic_error,
        'NotFound': _handle_generic_error,
        'MethodNotAllowed': _handle_generic_error,
        'NotAcceptable': _handle_generic_error,
        'AuthenticationFailed': _handle_generic_error,
        'ParseError': _handle_generic_error,
    }

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_generic_error(exc, context, response):
    response.data = errorResponse(status_code=response.status_code, error_code=response.data['detail'].code,
                                  message=response.data['detail'])
    return response


def _handle_request_error(exc, context, response):
    error_details = dict()
    error_message = ""
    for dat in response.data:
        ms = [f'{dat} field is required']
        msg = ms
        if dat != 'status_code' and dat != 'success' and dat != 'code' and dat != 'message':
            error_message = 'Bad request syntax or unsupported methods'
            error_details.setdefault(dat, msg)
        if dat == 'message':
            error_message = 'Duplicate entry'
            error_details.setdefault(dat, [response.data[dat]])

    response.data = {
        "error": True,
        "errors": [
            {
                "status_code": response.status_code,
                "error_message": error_message,
                "details": error_details
            }
        ]
    }
    return response


def _handle_authentication_error(exc, context, response):
    response.data = errorResponse(status_code=response.status_code, error_code=response.data['detail'].code,
                                  message="Authentications credentials were not provided or have expired")

    return response
