from rest_framework import status
from rest_framework.exceptions import APIException

class CustomError(APIException):
    status = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'CustomError'
    default_code = 'CustomError'

    def __init__(self, return_code = None, status_code = None, return_message = None):
        if return_code is None:
            return_code = '9999'
        if return_message is None:
            return_message = 'UNKONW_ERR'
        if status_code is None:
            self.status_code = status_code
        
        self.detail = {
            'return_code': return_code,
            'return_message': return_message,
        }