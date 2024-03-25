import psycopg
from psycopg.rows import Row
from .db_config import DB_CONNECTION


def run_db_statement(statement: str) -> list[Row]:
    conn_str = DB_CONNECTION
    if not conn_str:
        raise ValueError("'DB_CONNECTION' environment variable is not set.")

    # Connect to a database
    with psycopg.connect(conn_str) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(statement)
            return cur.fetchall()
