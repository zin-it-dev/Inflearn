from .extensions import api


class APIException(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


@api.errorhandler(APIException)
def handle_error(error):
    return {"message": error.message}, error.status_code
