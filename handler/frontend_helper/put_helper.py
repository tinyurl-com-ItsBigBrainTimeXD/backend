from Database.database import Database
from Core.ResponseBuilder import ResponseBuilder


def handle_put(serial_no: str, name: str, location: str, count: int, db: Database):
    """Handle the data"""
    if not db.get(serial_no):
        status_code = 404
    else:
        try:
            db.update(serial_no, name, count, location)
            status_code = 200
        except Exception as e:
            status_code = 500

    return ResponseBuilder(status_code).get_response()
        