class ResponseBuilder(object):
    def __init__(self, status_code: int, result = None):
        """Builder for the response"""
        self.status_code = status_code
        self.result = result

    def get_response(self):
        return {
            'result': self.result,
            'status_code': self.status_code
        }