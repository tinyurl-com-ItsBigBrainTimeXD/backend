import sqlite3


class Database(object):
    def __init__(self, db_path: str, table_name: str = 'items'):
        """Create the database object"""

        # Store the variables
        self.path = db_path
        self.table_name = table_name

        # Connect to the database
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

        # Initialise the table
        self.__init_table()

    def __init_table(self):
        """Initialise the table for the database if it does not exist"""

        # Execute the query to create a table if it does not exist
        self.__execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (serial_no INTEGER, name TEXT, count INTEGER, location TEXT)''')

    def __execute(self, sql_query: str, *args):
        """Execute the SQL_query"""

        # Execute the query
        self.cursor.execute(sql_query, args)
        return self.cursor.fetchall()

    def get_all(self):
        """Get all the items inside the table"""
        return self.__execute(f"SELECT * from {self.table_name}")

    def get(self, serial_no: int):
        """Get the relevant information in the database"""
        return self.__execute(f'SELECT * from {self.table_name} WHERE serial_no = ?', serial_no)

    def insert(self, serial_no: int, name: str, location: str, count: int = 1):
        """Insert the item into the database"""
        return self.__execute(f"INSERT into {self.table_name}(serial_no, name, count, location) VALUES(?, ?, ?, ?) ", serial_no, name, count, location)

    def delete(self, serial_no: int):
        """Remove the item in the database based on the id that is provided"""
        return self.__execute(f'DELETE from {self.table_name} where serial_no = ?', serial_no)

    def update(self, serial_no: int, name: str, count: int, location: str):
        """Update the item that is provided"""
        return self.__execute(f'UPDATE {self.table_name} SET name = ?, count = ?, location = ? WHERE serial_no = ?', name, count, location, serial_no)

    def search(self, keyword: str):
        """Search for the items in the database with the following keyword as name"""
        items = self.get_all()
        return list(filter(lambda x: keyword in x[1], items))

    def commit(self):
        """Commit the changes to the database"""
        self.db.commit()

    def __del__(self):
        """Save the files in the database"""
        self.commit()
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    db = Database('test.db')
    while True:
        inp = input("Command: ")
        if inp.lower() == 'q':
            break
        try:
            print(eval(inp))
        except Exception as e:
            print(type(e), e)
