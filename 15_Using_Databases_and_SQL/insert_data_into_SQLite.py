import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')

fop = open(fname)

for line in fop:
    line = line.rstrip()
    word = line.split()

    if len(word)<3 or word[0] != 'From':
        continue
    else:
        email = word[1]
        uni = email.split()
        uniname = uni[1]
        cur.execute('SELECT count FROM Counts WHERE email=?', (uniname,))
        row = cur.fetchone()  #Next line
        if row is None:
            cur.execute('INSERT INTO Counts (email, count) VALUES(?,1)', (uniname,))
        else:
            cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?', (uniname,))
        conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
