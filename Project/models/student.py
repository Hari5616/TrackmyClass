from database.operations import find_one,find

#using student_id searcha nd give details in students
def get_student_by_id(student_id):
    student_data=find_one('students',{'student_id':student_id})
    if student_data:
        student_data.pop('password',None)
        student_data.pop('_id',None)
    return student_data

#using student_id search and give course detail in enrollments collection and courses collection
# Get all courses a student is enrolled in Returns list of course details
def  get_student_courses(student_id):
    student_enrollment=find('enrollments',{'student_id':student_id})
    course_detail=[]
    for enrollment in student_enrollment:
        course=find_one('courses',{'course_id':enrollment['course_id']})
        course.pop('_id',None)
        course_detail.append(course)
    return course_detail

#using student_id find attendance in its collection
#Calculate overall attendance percentage for student  Returns percentage as float
def get_student_attendance_percentage(student_id):
    student_attendance=find('attendance',{'student_id':student_id})
    if not student_attendance:
        return 0.0
    present_days=len([clas for clas in student_attendance if clas['status']=='Present'])
    total_days=len(student_attendance)
    
    percentage=(present_days/total_days)*100
    return round(percentage,2)
    
#by student_id u can access grade after calculate 
#Get all grades for a student Returns list of grade records with course names
def get_student_grades(student_id):
    student_grades=find('grades',{'student_id':student_id})
    for grade in student_grades:
        course=find_one('course',{'course_id':grade['course_id']})
        if course:
            grade['course_name']=course['course_name']
        grade.pop('_id',None)
    return student_grades
    

def update_student_profile():
    pass

def change_password():
    pass