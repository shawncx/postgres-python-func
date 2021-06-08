import logging
import psycopg2
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    db_time = get_time_from_db()
    return func.HttpResponse(f"Hello, here's the time from db: {db_time}", status_code=200)

def get_time_from_db():
    conn_string = os.environ['POSTGRESQLCONNSTR_RESOURCECONNECTOR_TESTPYWEBAPPFUNCSECRETCONN_CONNECTIONSTRING']
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    rows = cursor.fetchall()
    return rows[0]
