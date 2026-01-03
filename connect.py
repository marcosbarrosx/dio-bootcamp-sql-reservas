from pathlib import Path
import sqlite3
import config


class databaseConnection:
    def __init__(self, db_path):
        self.db_path = Path(db_path)
        self.conn = None
        self.cursor = None
        self.isConnected: bool = False
        self.checkDbExist()

    # Establish a connection to the SQLite database, the parameter is the path to the database file
    def connectToDb(self):
        print(f'Connecting to database at {self.db_path}...')
        try:
            self.conn = sqlite3.connect(str(self.db_path))
            self.cursor = self.conn.cursor()
            self.isConnected = True
            print("Connection established.")
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database {self.db_path}: {e}")
        
    # Check if the database file exists
    def checkDbExist(self):
        print('Checking if database exists...')
        if not self.db_path.exists():
            raise FileNotFoundError(f"Database file does not exist: {self.db_path}")
        print('OK')
        return True
    
    # Close the database connection
    def closeConnection(self):
        if not self.isConnected:
            raise ConnectionError("No active database connection to close.")
        
        print('Closing database connection...')
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    @property
    def isConnected(self) -> bool:
        return self.isConnected
    @isConnected.setter
    def isConnected(self, value:bool):
        self.isConnected = value

class accessDatabase(databaseConnection):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.query = None

    def executeQuery(self, query: str):
        if not self.isConnected:
            raise ConnectionError("No active database connection.")
        self.cursor.execute(query)
                