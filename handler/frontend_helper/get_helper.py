from Database.database import Database
from Core.helpers import generate_number, is_blank


def search_handle(keyword: str, db: Database):
    """Handle the searching of data"""
    if keyword is None or len(keyword) == 0:
        raise KeyError('There is no keyword')
    return db.search(keyword)


def all_handle(keyword: str, db: Database):
    """Return all the values in the database
        Keyword is ignored.
    """
    return db.get_all()


def get_random_id_handle(keyword: str, db: Database):
    """Get a random ID
        keyword and database is ignored.
    """
    return generate_number()


get_dict = {
    1: all_handle,
    2: search_handle,
    3: get_random_id_handle,
}
