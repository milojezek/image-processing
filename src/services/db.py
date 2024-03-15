import os

import psycopg
from psycopg.rows import Row


def run_db_statement(statement: str) -> list[Row]:
    conn_str = os.getenv("DB_CONNECTION_STRING")
    if not conn_str:
        raise ValueError("`DB_CONNECTION_STRING` environment variable is not set.")

    # Connect to a database
    with psycopg.connect(conn_str) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(statement)
            return cur.fetchall()
