

#               CHAPTER 1 :  INSTALLING PSYCOPG2 AND BASIC CONNECTION 
# INSTALLATION 
"""
> pip install psycopg2-binary
""" 
# EXAMPLE-1 
"""
import psycopg2 as pg      # import psycopg2 module 
conn=pg.connect(           # connect to daatbase 
    host="localhost",
    database="institute",
    user="postgres",
    password="shivampythondev",
) 
cursor=conn.cursor()       # create a cursor to execute sql commands 



# close the cursor and conn
cursor.close()
conn.close()
"""

#     CHAPTER 2  : EXECUTING SQL COMMANDS FROM PYTHON

import psycopg2 as pg 
conn=pg.connect(
    host="localhost",
    database="demo",
    user="postgres",
    password="shivampythondev",
    port=5432
)
cursor=conn.cursor()
# CREATE TABLE 
'''
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS materials(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    quantity NUMERIC(20,4),
    rate NUMERIC(20,4)
    )
""")
conn.commit()
'''

# INSERT SINGLE DATA (I MEAN SINGLE ROW DATA )
'''
cursor.execute(""" 
   INSERT INTO materials(name,quantity,rate)
   VALUES (%s,%s,%s)
""",
('sand',45.45678,103.456789123)
)
conn.commit()
'''

# CHAPTER 3  :  READING DATAS FROM POSTGRESQL 

# fetchone()  - fetch one data from postgresql 
'''
cursor.execute("SELECT * FROM materials WHERE id=%s",(2,))
row=cursor.fetchone()    # returns in tuple form 
print(row[0],row[1],row[2],row[3])
'''

# fetchall()  -  or many datas 
"""
cursor.execute("SELECT * FROM materials")
rows=cursor.fetchall()
for row in rows:
    print(row)
"""

#   CHAPTER 4 :   TRANSACTIONS ( COMMIT AND ROLLBACK )
'''
conn.begin() dont exists, psycopg2 automatically handles that part.
BEGIN is automatic in psycopg2 (autocommit=False)
You just need conn.commit() or conn.rollback()
Use python try/except for transiction part.
Use cursor.close() and conn.close() inside finally of try/except.
'''
'''
try : 
    cursor.execute("UPDATE materials SET id=%s where id=%s",(500,99))    # works well
    cursor.execute("INSERT INTO materials(id,name,quantity,rate) VALUES (%s,%s,%s,%s)",(4,'steel_12mm',12,40))          # gives error cause 4 id already exists 
    conn.commit()                                             # save permanently if no error
except Exception as e:
    conn.rollback()                                           # undo sql commands if error found
    print(e)                                                  # print(error)
'''

# close the cursor and connection so postgreSQL server wont get messed up.
cursor.close()
conn.close()