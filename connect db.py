import MySQLdb
con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root",db="speech")

cur = con.cursor()

# Use all the SQL you like
cur.execute("CREATE TABLE asl( word varchar(20), sign varchar(100)")
