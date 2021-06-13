#mysql -u root -p
import mysql.connector

def GetData(FirstName, Feedback):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="3856",
        database="Journal"
    )

    mycursor=mydb.cursor()

    sql='INSERT INTO user_info (FirstName, Feedback) VALUES ("{0}", "{1}");'.format(FirstName, Feedback)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Record successfully inserted.")
