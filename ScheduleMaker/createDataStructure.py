import sqlite3 
import pandas as pd

# import react (probably for the interactive display)

# I am defining data structure as a class for the sql statements of the code
# in this model I used AI to guide me through a few possible ways ad came up with
# the first model that is a function to create the sql statements when necessary
# to modify the data structure such as change staff name, add shifts, all sorts
# that has to be done manually, it need improvment
# like this we can have it in the main code but only use when necessary

# class DataStructure:
def create_database(db_name, sql_statements):
    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    try:
        for statement in sql_statements:
            cursor.execute(statement)
            print(f"Executed: {statement}")

        conn.commit()
        print("Updated successfully!")
    except sqlite3.Error as error:
        print(f"Error while creating table -> {error}")
    finally:
        if conn:
            conn.close()
            print("The SQL connection is closed.")
sql_statements = [
        """
        CREATE TABLE IF NOT EXISTS StaffName(
	ID INT NOT NULL,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL
    );
    """
        ]

db_name = 'schedulerDatabase.db'

create_database(db_name, sql_statements)
