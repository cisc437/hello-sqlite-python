import sqlite3

con = sqlite3.connect('scrabble.sqlite')
cur = con.cursor()

sql = "select rack, words from racks where length=7 and weight <= 10 order by random() limit 0, 5"

cur.execute(sql)
results = cur.fetchall()

for res in results:
    print res

con.commit()
con.close()