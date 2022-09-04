import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# creating employees table
# c.execute("""CREATE TABLE employees(
#     first text,
#     last text,
#     pay integer
# )""")
# conn.commit()

# inserting values into table
c.execute("INSERT INTO employees VALUES ('John','Wick', 75000)")
conn.commit()

conn.close()