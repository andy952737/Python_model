import MySQLdb

db = MySQLdb.connect(host='localhost',user='username',passwd='password',db='demo_db')        
cur = db.cursor()
cur.execute('SELECT * FROM product')
for row in cur.fetchall():
    print row
db.close()