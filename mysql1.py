import mysql.connector
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="admin",database="mydb")
curs=con.cursor()
#curs.execute('create table student2(name varchar(100),age int,department varchar(100))')
#print("Table created successfully")
users=[("john",23,"CSE"),("suresh",34,"ECE"),("praveen",45,"ECE"),("mary",25,"CSE")]
curs.executemany("insert into student2(name,age,department) values(%s,%s,%s)",users)
con.commit()
print("Data inserted successfully")
curs.execute("select * from student2")
row=curs.fetchall()
con.close()
print("connection closed")