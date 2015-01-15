#!/usr/bin/env python
# collect name, age, home, sex from user. Save this data with MySQL


import MySQLdb

name = ''
age = ''
home = ''
sex = ''

db = MySQLdb.connect(host="localhost", user="root", passwd="-p", db="database_RateIT")
cur = db.cursor() 




def collectSet():
    global name, age, home, sex

    name = raw_input('Enter your name: ')
    age = raw_input('Enter your age: ')
    home = raw_input('Enter your home: ')
    sex = raw_input('Enter your sex: ')
    
    print ('set collected.')
    
    

#collectSet()  

# Use all the SQL you like
#cur.execute("SELECT * FROM test_table")

cur.execute("INSERT INTO table_contacts (name, age, sex, home) VALUES ('Cory','3','f','zeal');")


cur.close()




# print all the first cell of all the rows
# for row in cur.fetchall() :
# print row[0]
print 'done'





