def __handle_frontend_get(req_body):
    """Handle get requests from the frontend"""
    pass

def __handle_frontend_post(req_body):
    """Handle post requests from the frontend"""
    pass

def __handle_frontend_put(req_body):
    """Handle put request from the frontend"""
    pass

def __handle_frontend_delete(req_body):
    """Handle delete requests from the front end"""
    # Delete is disabled
    return __invalid_frontend_method(req_body)

def __invalid_frontend_method(req_body):
    """Invalid request method"""
    return f"""<h1> Invalid request</h1> <p>{req_body}</p>"""

handler_dict = {
    'post': __handle_frontend_post,
    'get': __handle_frontend_get,
    'put': __handle_frontend_put,
    'delete': __handle_frontend_delete,
    'invalid': __invalid_frontend_method
}

def frontend_handler(req_body: dict, req_type: str):
    """Handle the requests made from the front end"""
    handler = handler_dict.get(req_type, handler_dict['invalid'])