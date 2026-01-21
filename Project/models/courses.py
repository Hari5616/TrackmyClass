from database.operations import find_one,find
#Get all courses in database
def get_all_courses():
    courses=find('courses',{})
    for course in courses:
        course.pop('_id',None)
    return courses

#Get specific course by ID
def get_course_by_id(course_id):
    courses=find_one('courses',{'course_id':course_id})
    courses.pop('_id',None)
    return courses
    
#Get student's weekly timetable Returns organized schedule by day and time
def get_weekly_timetable(student_id):
    enrolled_courses=find('enrollments',{'student_id':student_id})
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    timetable= {day:[] for day in days}
    
    for enroll in enrolled_courses:
        course=find_one('courses',{'course_id':enroll['course_id']})
        
        if course:
            for class_time in course.get('schedule',[]):
                day=class_time['day']
                time=class_time['time']
                
                if day in timetable:
                    timetable[day].append({"time":time,
                                         "course_name":course['course_name'],
                                        'course_id':course['course_id'],
                                         "instructor": course.get('instructor', 'N/A')
                                          })
    for day in timetable:
        timetable[day].sort(key=lambda sort_time:sort_time['time'])
                
        
    return timetable
            