import sqlite3
import jwt
conn = sqlite3.connect('example.db')

cursor = conn.cursor() 
cursor.execute(" ""CREATE TABLE IF NOT EXISTS Users( id INT PRIMARY KEY, firstName TEXT, lastName TEXT, accountNumber TEXT, password TEXT, token TEXT) """)
conn.commit() 

try:
    user = [('1', 'fn', 'ln', '12','pass',''), ('2', 'fna', 'lna', '12a','passa',''), ('3', 'fns', 'lns', '12s','passs','')] 
    cursor.executemany("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?)", user) 
    conn.commit()
except:
    print("")

cursor=conn.cursor()
accnr = input('Enter your account number:')
passwd = input('Enter your password:')
data = cursor.execute("SELECT %s FROM Users where %s=? and %s=?" % ("firstName", "accountNumber", "password"), (accnr, passwd,))



if (len(data.fetchall()) == 0): 
    print("Invalid login")
else: 
    print("------ LOGAT =-----")
    key = 'secret' 
    encoded = jwt.encode({'exp':45, 'accountNumber': accnr }, key, algorithm='HS256') 
    cursor.execute("UPDATE Users SET %s=? WHERE %s=? AND %s=?" % ( "token", "accountNumber", "password"), (encoded, accnr, passwd,)) 
    conn.commit() 
    print('Login successful.') 
    print(encoded)
