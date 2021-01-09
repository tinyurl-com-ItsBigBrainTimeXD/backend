from handler.Iot_helper.device_state import DeviceState
from constants import device

def handle_get():
    """Handles get"""
    return {}

def iot_handler(req_type: str):
    """Handler for communication between the IoT devices"""
    result = handle_get()
    result.update(device.get_dict())
    print(result)
    if device.buzzer:
        device.buzzer = not device.buzzer
    return result
    