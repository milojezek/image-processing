import os

HOST = "host=" + os.getenv("HOST")
PORT = "port=" + os.getenv("PORT")
DB_NAME = "dbname=" + os.getenv("DATABASE")
DB_USER = "user=" + os.getenv("DB_USER")
DB_PASSWORD = "password=" + os.getenv("DB_PASSWORD")
SSL_MODE = "sslmode=require"

DB_CONNECTION = f"{HOST} {DB_NAME} {DB_USER} {DB_PASSWORD} {PORT} {SSL_MODE}"
