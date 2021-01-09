import base64
import datetime
from hashlib import sha256


def generate_number() -> str:
    """Generate a unique serial number"""
    # Generate a number
    no = sha256(datetime.datetime.now().ctime().encode())

    # Return the generated number
    return base64.b64encode(no.digest()).decode()


def is_blank(*string: str):
    """Checks if the string is blank"""
    return all(map(lambda x: (x is not None and len(x) > 0), string))

def is_blank_with_default(string: str, default: str):
    """Returns string if it is not blank otherwise return default value"""
    return default if is_blank(string) else string
