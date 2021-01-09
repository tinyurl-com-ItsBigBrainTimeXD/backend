
class JSONRequest(object):
    def __init__(self, request_body: dict):
        """Store the requests"""
        self.req_body = request_body

    def get(self, param: str):
        """Gets a parameter of the request body.
            returns None if the parameter is not found
        """
        return self.req_body.get(param, None)

    def get_key(self):
        """Get the key"""
        return self.get('key')

    def get_type(self):
        """Get the type of item"""
        return self.get('type')

    def get_serial_no(self):
        """Get the serial number in the json"""
        return self.get('serial_no')

    def get_location(self):
        """Get the location of the item"""
        return self.get('location')

    def get_name(self):
        """Get the name of the location"""
        return self.get('name')

    def get_count(self):
        """Get the count of the item"""
        return self.get('count')

    def get_image(self):
        """Get the image from the object"""
        return self.get('image')
