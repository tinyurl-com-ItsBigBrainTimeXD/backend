
class JSONRequest(object):
    def __init__(self, request_body: dict):
        """Store the requests"""
        self.req_body = request_body

    def get(self, param: str):
        """Gets a parameter of the request body.
            returns None if the parameter is not found
        """
        return self.req_body.get(param, None)