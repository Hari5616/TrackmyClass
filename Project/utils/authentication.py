import bcrypt
from database.operations import find_one

#We use this when we seed the data
def hash_password(plain_text):
  salt=bcrypt.gensalt()
  return bcrypt.hashpw(plain_text.encode('utf-8'),salt)

def verify_password(plain_text,password_hashed):
  return bcrypt.checkpw(plain_text.encode('utf-8'),password_hashed) 

def login(student_id,password):
  student=find_one('students',{'student_id':student_id})
  if student and verify_password(password,student['password']):
    student.pop('password',None)
    student.pop('_id',None)
  return student
  
print(login('STU002','password123'))

#plain_text.encode('utf-8') for making it to byte form for brcypt