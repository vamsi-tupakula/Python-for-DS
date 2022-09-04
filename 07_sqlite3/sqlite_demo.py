import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Employee class instance
emp_1 = Employee('Chris', 'Evans', 100000)

# creating employees table
# c.execute("""CREATE TABLE employees(
#     first text,
#     last text,
#     pay integer
# )""")
# conn.commit()

# inserting values into table
# c.execute("INSERT INTO employees VALUES ('John','Wick', 75000)")
# conn.commit()

# inserting employee class instance values
c.execute("INSERT INTO employees VALUES ('{}','{}', {})".format(emp_1.first,emp_1.last,emp_1.pay))
conn.commit()

# deleting in sql
# c.execute("DELETE FROM employees WHERE first = 'John'")
# conn.commit()

# retreive values in the table
c.execute('SELECT * FROM employees')
# print(c.fetchone())
print(c.fetchall())

conn.commit()

conn.close()