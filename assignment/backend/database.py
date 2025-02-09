import os
import psycopg2
from psycopg2 import sql

DATABASE_URL = os.getenv('postgresql://postgres:post12398@db:5432/postgres')

def get_db_connection():
    # return psycopg2.connect(DATABASE_URL)
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="post12398",
        host="db",  # Ensures connection via TCP/IP instead of Unix socket
        port=5432
    )