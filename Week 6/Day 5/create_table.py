import psycopg2
from datetime import date
USERNAME = "postgres"
PASSWORD = "daza"
DATABASE = "hollywood"
HOSTNAME = "localhost"

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

cursor = connection.cursor()


def run_query(query):
    cursor.execute(query)
    output = None
    try:
        output = cursor.fetchall()
    except:
        connection.commit()

    return output


query1 = "select * FROM actors;"
query2 = "select * from actors where last_name = 'Krasinsky';"

print(run_query(query1))


title = "Titanic"
release_date = date(2002, 10, 12)
actor = 5

query3 = f"INSERT INTO movies (title, release_date, actor) values ('{title}', '{release_date}', {actor});"

run_query(query3)