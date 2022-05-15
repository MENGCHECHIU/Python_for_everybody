import sqlite3

#建立資料庫
conn=sqlite3.connect("emaildb.sqlite")

#建立cursor變數
cur=conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

#建立table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname=input("Enter file name:")
fh = open(fname)
for line in fh :
    if not line.startswith("From: "): 
        continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    #選擇資料
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    #取得資料
    row = cur.fetchone()

    # insert 或 update 資料 

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES (?, 1)''', (org,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()