import sqlite3
#If you are creating a datatbase for first time then you should import os
import os
os.system('clear')
'''
This will connect a database named "database". If there is no database named "database"
then python will create a new database named by "database".
'''
conn = sqlite3.connect('database.db')
c = conn.cursor()
'''
This will create a table in that database by which the columns will be named. You can create your own names. You won't need
to type this create table again.
'''
c.execute("""CREATE TABLE databases(
            in_name text,
            in_age text,
            ph_number text,
            select_state text
            )""")

conn.commit()

conn.close()
