from Database.database import Database


def handle_get():
    """Handle getting of image
        Signal whether to sound the buzzer 
    """
    pass

def handle_post():
    """Handle getting
        Send status of box to the server
    """
    pass

handler_dict = {
    'get': handle_get,
    'post': handle_post,
}


def iot_handler(req_body: dict, req_type: str, db: Database):
    """Handler for communication between the IoT devices"""
    return None
