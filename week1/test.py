import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=ny_taxi port=5432 user=root password=root")
    conn.close()
except psycopg2.OperationalError as ex:
    print("Connection failed: {0}".format(ex))