from django.db import models
from apps.classroom.models import ClassEnvironment, Lesson, Notification
from apps.userprofile.models import HomeworkflowUser, Student, Teacher, Parent

absent_types = {
    "late":"late",
    "absent":"absent",
}

behaviour = {
    "excellent":"excellent",
    "good":"good",
    "average":"average",
    "poor":"poor"
}

class Attendance(models.Model):
    date = models.DateField()
    student_id = models.ForeignKey(Student)
    type = models.CharField(choices=absent_types)
    lesson_id = models.ForeignKey(Lesson)

class Homework(models.Model):
    lesson_id = models.ForeignKey(Lesson)
    due_date = models.DateField()
    description = models.TextField()
    # Constraint: due date in future
    # class Meta:
    #     models.CheckConstraint(
    #             name='%(app_label)s_%(class)s_due_date_in_future_check',
    #             check=models.Q(due_date__gt=models.F('current_date'))
    #         ),


class Homework_Uncompleted(models.Model):
    homework_id = models.ForeignKey(Homework)
    student_id = models.ForeignKey(Student)

class Weekly_Feedback(models.Model):
    student_id = models.ForeignKey(Student)
    teacher_id = models.ForeignKey(Teacher)
    homework_completion = models.ForeignKey(Homework_Uncompleted) #get average by student id
    #sum(student_id) of homework_uncompleted
    attendance_rate = models.ForeignKey(Attendance)  #get average by student id
    date_created = models.DateField(auto_now_add=True)
    written_feedback = models.TextField()
    social_behaviour = models.CharField(choices=behaviour)
    work_ethics = models.CharField(choices=behaviour)
    parent_checked = models.BooleanField(default=False)
