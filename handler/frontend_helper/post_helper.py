from Database.database import Database
from Core.ResponseBuilder import ResponseBuilder
from Core.helpers import is_blank


def handle_post(serial_no: str, name: str, location: str, count: int, db: Database) -> dict:
    """Handle the insertion of new data"""
    try:
        if db.get(serial_no):
            status_code = 404
        else:
            db.insert(serial_no, name, location, count)
            status_code = 200
    except Exception as e:
        status_code = 500

    return ResponseBuilder(status_code).get_response()
