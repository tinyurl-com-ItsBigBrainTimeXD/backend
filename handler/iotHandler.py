from handler.Iot_helper.device_state import DeviceState
from constants import device

def handle_get(req_body):
    """Handles get"""
    return {}

def handle_invalid(req_body):
    """"""
    return {
        "result": 'Invalid data'
        }

handler_dict = {
    'get': handle_get,
    'invalid': handle_invalid
}


def iot_handler(req_body: dict, req_type: str):
    """Handler for communication between the IoT devices"""
    handler = handler_dict[req_type.lower()]
    result = handler(req_body)
    result.update(device.get_dict())
    if device.buzzer:
        device.buzzer = not device.buzzer
    return result
    