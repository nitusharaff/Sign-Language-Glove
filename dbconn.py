import MySQLdb
con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root")
db1 = con.cursor()
db1.execute('CREATE DATABASE speech')

db1.execute("CREATE TABLE asignl( word varchar(20), sign varchar(100)")
