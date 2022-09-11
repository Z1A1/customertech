import mysql.connector
#def DataUpdate(name,amt,account,time,transfer):
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="schoolqa",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customercare (name CHAR(255), email  VARCHAR(255), phone_number  VARCHAR(255) )") 
     #sql='INSERT INTO customers (name,amt,account,time,transfer) VALUES ("{0}","{1}", "{2}","{3}","{4}");'.format(name,amt,account,time,transfer)
     #mycursor.execute(sql)
     #mydb.commit() 

    

