# pylint: disable=C0114, W0311, C0301
import os
from dotenv import load_dotenv
import pymysql

class SQLManager(object):
	"""
    This is a utility class for managing SQL connections and executing queries.
	"""

	def __init__(self):
		"""
		Initializes the SQLManager object.
		"""
		self.conn = None
		self.cursor = None
		self.connect()

	def connect(self):
		"""
        Establishes a connection to the database.
        """
		load_dotenv()
		self.conn = pymysql.connect(
			host = os.getenv('DB_HOST'),
			port = int(os.getenv('DB_PORT')),
			user = os.getenv('DB_USER'),
			password = os.getenv('DB_PASSWORD'),
			db = os.getenv('DB_NAME')
        )
		self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

	def get_list(self, sql, args=None):
		"""
        Executes a query and retrieves a list of results.
        
        Args:
            sql (str): The SQL query to execute.
            args (tuple, optional): The query parameters (placeholders) for the SQL query.

        Returns:
            list: A list of dictionaries representing the query results.
        """

		self.cursor.execute(sql, args)
		result = self.cursor.fetchall()
		return result

	def get_one(self, sql, args=None):
		"""
        Executes a query and retrieves a single result.
        
        Args:
            sql (str): The SQL query to execute.
            args (tuple, optional): The query parameters (placeholders) for the SQL query.

        Returns:
            dict: A dictionary representing the query result.
        """
		self.cursor.execute(sql, args)
		result = self.cursor.fetchone()
		return result

	def moddify(self, sql, args=None):
		"""
        Executes a single SQL statement for modification (e.g., INSERT, UPDATE, DELETE).
        
        Args:
            sql (str): The SQL statement to execute.
            args (tuple, optional): The query parameters (placeholders) for the SQL statement.
        """
		self.cursor.execute(sql, args)
		self.conn.commit()

	def multi_modify(self, sql, args=None):
		"""
        Executes multiple SQL statements for modification (e.g., INSERT, UPDATE, DELETE).
        
        Args:
            sql (str): The SQL statement to execute.
            args (list, optional): A list of tuples containing the query parameters (placeholders) for the SQL statements.
        """
		self.cursor.executemany(sql, args)
		self.conn.commit()

	def create(self, sql, args=None):
		"""
        Inserts a new record into the database and returns the last inserted ID.
        
        Args:
            sql (str): The SQL statement to execute.
            args (tuple, optional): The query parameters (placeholders) for the SQL statement.

        Returns:
            int: The last inserted ID.
        """
		self.cursor.execute(sql, args)
		self.conn.commit()
		last_id = self.cursor.lastrowid
		return last_id

	def close(self):
		"""
        Closes the database connection.
        """
		self.cursor.close()
		self.conn.close()

	def __enter__(self):
		"""
        Enables the SQLManager object to be used with the 'with' statement.
        """
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""
        Cleans up resources when exiting the 'with' statement.
        """
		self.close()
