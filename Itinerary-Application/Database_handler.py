import MySQLdb as pdb


def connection():
    credentials = {
      'mysql': {
          'host': 'mysql-db.cbvvxkzv412m.us-east-1.rds.amazonaws.com',
          'username': 'admin',
          'password': 'database',
          'database': 'Itenary_DB'
      }
    }

    db_host = credentials['mysql']['host']
    db_username = credentials['mysql']['username']
    db_password = credentials['mysql']['password']
    db_name = credentials['mysql']['database']

    return pdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_name)


def write():
    conn = connection()
    cursor = conn.cursor()

    c1 = 'user1'
    c2 = 'Jayalakshmi'
    c3 = 'Vijayan'
    c4 = '26'
    c5 = 'jayalakshmi.e.mec@gmail.com'
    c6 = '07879985444'

    cursor.execute(
        "INSERT INTO users values('{userid}','{name}', '{surname}', '{age}', '{emailid}', '{mobile}');".format(
            userid=c1, name=c2, surname=c3, age=c4, emailid=c5, mobile=c6))

    conn.commit()
    conn.close()


def read():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("select * from users")
    read = cursor.fetchall()

    for x in read:
        print(x)

    conn.close()


def modify_table():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("ALTER  TABLE Itenary_DB.users ADD (age INT)")

    conn.close()
