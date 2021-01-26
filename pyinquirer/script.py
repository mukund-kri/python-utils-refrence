from PyInquirer import prompt, print_json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect("dbname=postgres user=admin password=password host=localhost")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

dbs_query = 'SELECT datname FROM pg_database WHERE datistemplate = false'

cur.execute(dbs_query)

databases = map(lambda row : row[0], cur.fetchall())


questions = [
    {
        'type': 'checkbox',
        'name': 'databases',
        'message': 'Select the Databases you want to delete',
        'choices': [{'name': db} for db in databases]
    }
]

answers = prompt(questions)

for db in answers['databases']:
    cur.execute(f'DROP DATABASE {db}')

conn.commit()
cur.close()
conn.close()
