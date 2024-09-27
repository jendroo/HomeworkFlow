# Project Design

## Business Idea

### Problem Statement

While there a various platforms to manage online classes and courses, there are not really many tools to help with the management of traditional school classes.

Observing the school (german) landscape, you will quickly realize that most tasks are still handled manually in the traditional way. Giving feedback to students, assign and review homework, get in touch with parents and so on. Often parents don't realize on time that their kid is not on track.


## Solution Statement

Provide an online platform where the main-teacher can manage his/her class, assign and review homework, track the the students progress and attendence and have the opportunity to contact the parents. 

- Classes Set up by Database
- Teacher can assign homework
- Teacher checks for completion
- Easy way to get in touch with parent or vice versa
- Teachers and parents get to track progress of the child
- Teachers and parents can keep up with attendance
- Parents can keep track of children's progress
- Weekly evaluation 
- (Reward System)

## Business Objectives
- Easily connects teachers, students, parents
- Give an organised structure for learning and reviewing
- Facilitating the students in doing homework.
- (Motivate students with reward system)



# Requirements
## Functional Requirements

- Administration 
- Creation of student / teacher profiles by software
- Login
- Logout
- Teachers can create homework
    - Checks for completion phyiscally (inspired by german school system)
    - Marks as completed
- Teachers create important dates (tests, holidays, class trips etc.)
    - For tests: After correcting, puts grade into app.
- Teachers review weekly student report
    - Adds feedback to field
- Teachers have quick contact data for parent (if provided: usually email & phone)

- Students
    - Can view their homework
    - Can view their lessons
    - Can view their notification
    - Get their weekly reports

- Parents
    - Can view children's performance
    - Can view children's weekly report
    - Quick access to contact data (email button -> write email)


## Non-Functional Requirements
- Authentication will be Token based
- API as a Service built on REST API with Django Rest Framework (DRF)
- It will be deployed on Railway
- API testing via Postman


## Database Design
- Data about teachers, classes and students provided by school
- Entering, editing, maintaining data
- Extracting information from the database

# Database Mission Statement
Create classes based one school data, generate user profiles and maintain data that will make handling student progress effective and smooth.


## Database Mission Objectives
- Classes created based on school data
- Create homework between teacher and student
- 

# Requirement
- Teacher
    - teacher_id 
    - username
    - first_name
    - last_name
    - password
    - email
    - main_class_id
    

- Student
    - username
    - first_name
    - last_name
    - password
    - email
    - class_id
    
- Parent
    - username
    - first_name
    - last_name
    - password
    - email
    - student_id

- Homework
    - lesson_id
    - due_date
    - description
    


- Class
    - teacher: Teacher

- Subjects
    - subject_id
    - subject_name

- Notification/Dates
    - name 
    - date
    - description
    - class_id

- Lesson   

- Attendance
    - date
    - student_id
    - type(late, absent)


- Weekly_feedback
    - student_id:
    - teacher_id
    - homework complete:
        aggregate function: average(status)
    - attendance:
        - Has been late: x times (count where type = attendance.type = late)
        - Has been absent: x times (count where type = attendance.type = absent)
            - if both are 0:
                    - 100% attendance

    - teacher_written_feedback: textfield
    - date/working_week: date
    

Questions:
Can we assume "lessons" are already put into the system?
- Are lessons created by the (school)-admin or the teacher himself?
    - Teacher gets his timetable at beginning of the year and creates puts his own lessons

- is main_class_id enough to give extra "priviliges"?

- Roles: Do we need extra "roles" or can we implement it from tables

- Messages in API endpoints - when are they needed ? Only for error messages?

- Look for Django Sessions over Token Authorization


- Migration Ordering (can be done all at once?)
- on_delete
- homework & attendance fields in weekly report


- Probably have to change:
    - User models
        Right now: Have to create user and then student/teacher/parent individually
        Ideal: Create user, choose student/teacher/parent
        Question: Do we create students first or parents?
            - Cause right now we need to create parents first, which is probably not ideal.

    - Weekly_Feedback
        - Should homework_completion and attendance_rate just be FlowFields instead of ForeignKey?
        - Do you need a relation at all, if you fetch the value in the view?

    - role field neccessary?
    - student




































### Notes
tests = {
    
    date:"23/01/2024 8-14"
    subject:"maths"
    grade:"1"
}



homework = {
    student_id:1,
    homework_id:1,
    start_date:"01/01/2024 10:30:10",
    due_date:"01/01/2024 10:30:10",
    status:"completed",
}

Student has completed 80% of his homework. -> Homework Table
Student has had 100% attendance. -> Attendace Table
Student has written one test -> Event table

Written Teacher feedback: "Very good job, especially failing the maths test" -> 
Status (for parent): Unread / Read. -> 










NB: Think of something "beneficial/motivating" for the students
NB: Quickly touch on german school system in presentation.
