import psycopg2 as pg

class ConnectionFactory:
    def get_connection(self):
        '''Database Connection Function.

        This function serves as an entry point to establish a connection to the database. Make sure to replace the placeholders with specific data from your environment.

        Parameters:
            - host (str): The database server's address.
            - username (str): The username for authentication.
            - password (str): The user's password for authentication.
            - database (str): The name of the database you want to access.

        Returns:
            - conn: The established database connection.
            - cursor: The cursor for executing SQL queries.

        Example Usage:
            conn, cursor = connect_to_database('your_host', 'your_username', 'your_password', 'your_database')
            cursor.execute('SELECT * FROM example_table')
            results = cursor.fetchall()
            conn.close()
        '''
        
        return  pg.connect(host='Host', database='database', user='user', password='password')