import base64
from constants import device
from Database.database import Database
from Core.ResponseBuilder import ResponseBuilder


def handle_img_post(image_b64: str) -> dict:
    """Handle the img recognition for the item"""
    img_data = base64.b64decode(image_b64)
    with open('temp.jpg', 'wb') as file:
        file.write(img_data)
    return ResponseBuilder(200, 'bottle').get_response()
    

def handle_post(serial_no: str, name: str, location: str, count: int, db: Database) -> dict:
    """Handle the insertion of new data"""
    try:
        if db.get(serial_no):
            status_code = 404
        else:
            db.insert(serial_no, name, location, count)
            status_code = 200
            
    except Exception:
        status_code = 500

    return ResponseBuilder(status_code).get_response()

def handle_iot_post(buzzer: bool, lock: bool):
    device.toggle_lock()
    device.toggle_buzzer()
    return ResponseBuilder(200, device.get_dict()).get_response()
