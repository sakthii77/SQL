#access db with python


import sqlite3

connection = sqlite3.connect(r"C:\Users\s\desktop\test.db")
cursor=connection.cursor()

#ddl
#table creation

cursor.execute("Create table data(name varchar,id integer);")

#dml
#insert data

cursor.execute("insert into data(name,id) values('sakthi','1');")
connection.commit()

#view data

cursor.execute("select * from data")
a=cursor.fetchall()
print(i)

#update data

cursor.execute("update data set name='gopal' where name='sakthi';")
cursor.execute("select * from data")
a=cursor.fetchall()
for i in a:
	print(i)
	
#delete data	
	
cursor.execute("delete from data where name='gopal';")
cursor.execute("select * from data")
a=cursor.fetchall()
for i in a:
	print(i)
	
#ddl

#add a coloum

cursor.execute("alter table data add column text;")
cursor.execute("select * from data")
a=cursor.fetchall()
for i in a:
	print(i)

	
#drop a column

cursor.execute("alter table data drop column column;")
cursor.execute("select * from data")
a=cursor.fetchall()
for i in a:
	print(i)

#change the data type of a column

cursor.execute("alter table data alter column name integer;")

#drop the table
cursor.execute("drop table data;")

#clear the table


cursor.execute("Create table saro(name varchar,id integer);")
cursor.execute("insert into saro(name,id) values('sakthi','1');")
connection.commit()
cursor.execute("truncate table saro;")