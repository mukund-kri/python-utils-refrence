HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'


import _mysql


def connect(db=''):
    try:
        db = _mysql.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD, 
            db=db
            )
    except Exception, e:
        print e
    return db


def show_dbs(conn):
    conn.query('SHOW DATABASES')
    result = conn.store_result()
    print result.fetch_row(maxrows=0)


def create_db(conn, dbname, user):
    
    try:
        conn.query(
            "CREATE DATABASE %s" % dbname
            )
    except:
        print "DB exists"
        
    try:
        conn.query(
            "GRANT ALL PRIVILEGES ON  %s.* TO '%s'@'localhost'" % (dbname, user))
    except Exception, e:
        print e

def check_or_create_user(conn, user):
    conn.query(
        "SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '%s')" %
        user)
    result = conn.store_result()
    if result.fetch_row()[0][0] == '0':
        print "Creating new user %s" % user
        conn.query("CREATE USER '%s'@'localhost' IDENTIFIED BY 'password'" % user)

    
def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('db', help='name of the database to create')
    parser.add_argument('owner', 
                        help='owner of the newly create db')

    args = parser.parse_args()
    if not args.db:
        parser.error('the name of the db is compulsury')
    if not args.owner:
        parser.error('the db owner name is compulsury')
    return args.db, args.owner


if __name__ == '__main__':
    dbname, user = parse_args()


    conn = connect()
    check_or_create_user(conn, user)
    create_db(conn, dbname, user)


        

 

