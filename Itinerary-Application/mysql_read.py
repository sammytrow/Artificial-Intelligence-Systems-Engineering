import MySQLdb as pdb
from mysql_config import credentials as secrets

db_host = secrets['mysql']['host']
db_username = secrets['mysql']['username']
db_password = secrets['mysql']['password']
db_name = secrets['mysql']['database']

conn = pdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_name)
cursor = conn.cursor()

cursor.execute("select * from users")
read = cursor.fetchall()

for x in read:
    print(x)

conn.close()
