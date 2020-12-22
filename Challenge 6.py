#Quincy Asemota
#Weekly Assignment 9

import sqlite3
import codecs

#Welcome Message
def print_header():
    print('This program is designed to create a student databe for SUNY undergraduate body.')
    print('The program will create a student database and will populate it with random values for each student - id, firstname, surname, class, major and minor.')
    print('{0:<8} {1:<8} {2:<8} {3:<8} {4:<14} {5:<12} {6:<10} {7:<15} {8:<15}'.format("GPA","INF108","INF308","ID","Firstname","Surname","Class","Major","Minor")) 

def print_students_row(row):
  print('{0:<8.2f} {1:<8} {2:<8} {3:<8} {4:<14} {5:<12} {6:<10} {7:<15} {8:<15}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

print('====== Final grades for the Informatics students. ======')

conn = sqlite3.connect('wa9-students.sqlite')
cur = conn.cursor()

grades = [0.0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
grade_list = []

print('====== Creating INF 108 Table ======')

#Creating the INF a database
cur.execute('DROP TABLE IF EXISTS INF108')
cur.execute('CREATE TABLE INF108 (ID INTEGER, Grade REAL)')

# Student IDs in Informatics (major or minor)
id_list = []
cur.execute("SELECT * FROM students WHERE major='Informatics' OR minor='Informatics'")
for row in cur:
  id_list.append(row[0])

# Inserts Grade & ID 
for idx in id_list:
  # Random choice - grades
  grade = random.choice(grades)
  grade_list.append(grade)
  cur.execute('INSERT INTO INF108 (ID, Grade) VALUES (?, ?)',(idx, grade))
conn.commit()

# Creating the INF308 table
cur.execute('DROP TABLE IF EXISTS INF308')
cur.execute('CREATE TABLE INF308 (ID INTEGER, Grade REAL)')

# Collect student IDs in Informatics
id_list = []
cur.execute("SELECT * FROM students WHERE (major='Informatics' OR minor='Informatics') AND (class='Junior ' OR class='Senior')")
for row in cur:
  id_list.append(row[0])

# Insert ID, Grade to the table
for idx in id_list:
  # randomly choose grade from possible grade values
  grade = random.choice(grades)
  grade_list.append(grade)
  cur.execute('INSERT INTO INF308 (ID, Grade) VALUES (?, ?)',(idx, grade))
conn.commit()

# Average grade of Informatics students
print('The average grade of the Informatics students is ' + str(round(sum(grade_list)/len(grade_list),2)))

print('GPA score and related information of Seniors majoring in Informatics')

# Informatics Students and Senior and their grades
sql = "SELECT (INF108.Grade+INF308.Grade)/2 as GPA, INF108.Grade, INF308.Grade, students.* FROM students JOIN INF108 on students.ID = INF108.ID JOIN INF308 on students.ID = INF308.ID WHERE  major = 'Informatics' AND class='Senior'"
cur.execute(sql)
print_header()  
print("--------------------------------------------------------------------------------------------------------------------")
for row in cur:
  print_students_row(row)

cur.close()




