from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

#db_string = "sqlite:///tests.db"

db = create_engine(db_string)  
base = declarative_base()

class Teacher(base):  
#Define table name and column name   
  __tablename__ = 'students'
  stdid = Column(String, primary_key = True)
  stdname = Column(String)
  subjects = Column(String)
  marks = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

#Teacher.__table__.drop(db)
#Create
val1 = Teacher(stdid = '10001', stdname = 'std1', subjects = 'Maths', marks = '100')
val2 = Teacher(stdid = '10002', stdname = 'std2', subjects = 'Physics', marks = '80')
val3 = Teacher(stdid = '10003', stdname = 'std3', subjects = 'English', marks = '65')
val4 = Teacher(stdid = '10004', stdname = 'std4', subjects = 'Social', marks = '95')
val5 = Teacher(stdid = '10005', stdname = 'std5', subjects = 'Chemistry', marks = '99')

session.add(val1)
session.add(val2)
session.add(val3)
session.add(val4)
session.add(val5)
#session.commit()

#Read

students = session.query(Teacher)
s = []
for i in students:
  s.append([i.stdid, i.stdname, i.subjects, i.marks])
print(s)


#Update
val5.subjects = 'Language'
q = [val5.stdid, val5.stdname, val5.subjects, val5.marks]
#session.commit()
print(q)

#Delete
session.delete(val5)
students = session.query(Teacher)
e = []
for i in students:
  e.append([i.stdid, i.stdname, i.subjects, i.marks])
print(e)
#session.commit()



s=str(s)
q=str(q)
e=str(e)
with open(".hidden.txt",'w') as f:
	f.write(s)
	
with open(".hidden1.txt",'w') as f:
	f.write(q)

with open(".hidden2.txt",'w') as outfile:
	outfile.write(e)
