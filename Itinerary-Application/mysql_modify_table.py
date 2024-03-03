import MySQLdb as pdb
from mysql_config import credentials as secrets

# assignments
db_host = secrets['mysql']['host']
db_username = secrets['mysql']['username']
db_password = secrets['mysql']['password']
db_name = secrets['mysql']['database']

# create a connection to the database
conn = pdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_name)

# create a object for the queries we will be using
cursor = conn.cursor()

cursor.execute("ALTER  TABLE Itenary_DB.users ADD (age INT)")

conn.close()

