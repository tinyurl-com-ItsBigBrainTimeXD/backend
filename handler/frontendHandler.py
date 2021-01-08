import logging
from Database.database import Database
from Core.JSONRequest import JSONRequest
from handler.frontend_helper.get_helper import get_dict


# Set up logging
log = logging.getLogger(__name__)


def __handle_frontend_get(req_body: JSONRequest, db: Database):
    """Handle get requests from the frontend"""
    log.info(f"Get request received data: {req_body}")

def __handle_frontend_post(req_body: JSONRequest, db: Database):
    """Handle post requests from the frontend"""
    log.info(f"Post request received data: {req_body}")
    return f"POST: {req_body}"


def __handle_frontend_put(req_body: JSONRequest, db: Database):
    """Handle put request from the frontend"""
    log.info(f"Put request received data: {req_body}")
    return f"PUT: {req_body}"


def __handle_frontend_delete(req_body: JSONRequest, db: Database):
    """Handle delete requests from the front end"""
    log.info(f"Delete request received data: {req_body}")
    # Delete is disabled
    return __invalid_frontend_method(req_body)


def __invalid_frontend_method(req_body: JSONRequest, db: Database):
    """Invalid request method"""
    log.info(f"Invalid request method received data: {req_body}")
    return f"""<h1> Invalid request</h1><br><p>{req_body}</p>"""


handler_dict = {
    'post': __handle_frontend_post,
    'get': __handle_frontend_get,
    'put': __handle_frontend_put,
    'delete': __handle_frontend_delete,
    'invalid': __invalid_frontend_method
}


def frontend_handler(req_body: dict, req_type: str, db: Database):
    """Handle the requests made from the front end"""

    # Get the appropriate handler for the type of request
    handler = handler_dict.get(req_type.lower(), handler_dict.get('invalid'))

    # Create the JSONRequest class
    json_class = JSONRequest(req_body)

    # Execute the handler
    return handler(json_class, db)
