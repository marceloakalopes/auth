import pypyodbc as odbc
from env import connection_string  # Importing connection string from env.py file

def is_username_available(username: str) -> bool:
    """
    Checks if the given username is available in the database.

    Args:
        username (str): The username to check for availability.

    Returns:
        bool: True if the username is available, False otherwise.
    """
    conn = odbc.connect(connection_string)  # Establishing connection to the database

    QUERY = f"SELECT * FROM Records WHERE username = '{username}'"  # SQL query to check for username availability

    cursor = conn.cursor()

    try:
        cursor.execute(QUERY)  # Executing the SQL query
        rows = cursor.fetchall()
        if len(rows) == 0:
            raise Exception()
        print("Username already taken")
        return False  # Username is already taken
    except:
        return True  # Username is available
    

def register(user_name: str, password: str) -> bool:
    """
    Registers a new user with the provided username and password.

    Args:
        user_name (str): The username of the new user.
        password (str): The password of the new user.

    Returns:
        bool: True if the registration is successful, False otherwise.
    """
    if is_username_available(user_name):  # Checking if the username is available
        conn = odbc.connect(connection_string)  # Establishing connection to the database

        QUERY = f"""
                    INSERT INTO Records (username, password)
                    VALUES ('{user_name}', '{password}')
                """  # SQL query to insert new user into the database

        cursor = conn.cursor()

        cursor.execute(QUERY)  # Executing the SQL query to insert new user
        cursor.commit()
        cursor.close()

        return True  # Registration successful
    return False  # Registration unsuccessful because username is not available
    
   
def login(usr: str, pwd: str) -> bool:
    """
    Logs in a user with the provided username and password.

    Args:
        usr (str): The username of the user trying to log in.
        pwd (str): The password of the user trying to log in.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    conn = odbc.connect(connection_string)  # Establishing connection to the database

    QUERY = f"SELECT * FROM Records WHERE username = '{usr}'"  # SQL query to fetch user with provided username

    cursor = conn.cursor()

    try:
        cursor.execute(QUERY)  # Executing the SQL query
        rows = cursor.fetchall()
        credentials = rows[0]
        if credentials[0] == usr and credentials[1] == pwd:
            print("Success")
            return True  # Login successful
        else:
            raise Exception()

    except:
        print("No user found with matching email")
        return False  # No user found with matching email or incorrect password
