import MySQLdb as pdb
from mysql_config import credentials as secrets
import random
import datetime

db_host = secrets['mysql']['host']
db_username = secrets['mysql']['username']
db_password = secrets['mysql']['password']
db_name = secrets['mysql']['database']

conn = pdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_name)

cursor = conn.cursor()

c1 = 'user1'
c2 = 'Jayalakshmi'
c3 = 'Vijayan'
c4 = '26'
c5 = 'jayalakshmi.e.mec@gmail.com'
c6 = '07879985444'

cursor.execute("INSERT INTO users values('{userid}','{name}', '{surname}', '{age}', '{emailid}', '{mobile}');".format(userid = c1, name=c2, surname=c3, age=c4, emailid=c5, mobile = c6))

conn.commit()
conn.close()
