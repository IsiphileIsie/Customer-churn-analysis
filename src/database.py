import sqlite3
from pathlib import Path
import pandas as pd


def connect_to_database():
    """
    Establish a connection to the customer churn SQLite database.
    """
    project_root = Path(__file__).resolve().parent.parent
    database_path = project_root / "database" / "customer_churn.db"

    connection = sqlite3.connect(database_path)

    return connection



def load_customer_data():
    """
    Load customer records from the SQLite database into a DataFrame.
    """
    connection = connect_to_database()

    try:
        query = "SELECT * FROM customers"
        data = pd.read_sql_query(query, connection)
        return data

    finally:
        connection.close()



def read_query(query):
    """
    Execute a SQL query and return the results as a DataFrame.
    """
    connection = connect_to_database()

    try:
        data = pd.read_sql_query(query, connection)
        return data

    finally:
        connection.close()