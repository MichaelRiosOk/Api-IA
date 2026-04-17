import pyodbc
from app.config import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_USERNAME,
    SQL_PASSWORD,
    SQL_DRIVER,
)


def get_connection():
    connection_string = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)


def execute_query(query: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))

        return result
    finally:
        cursor.close()
        conn.close()