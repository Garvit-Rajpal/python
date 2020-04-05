import pymysql
db=pymysql.connect('localhost','root','1805','garv')
cursor=db.cursor()
sql="""INSERT INTO table1(FIRST_NAME,
           LAST_NAME,AGE,SEX,INCOME)
           VALUES('DEVA','BHAND',19,'T','123445676578557656')"""
try:
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()
    
    
print("INSERTED")
db.close()
