from django.db import models

    
class Teacher(models.Model):
    teacher_first_name=models.CharField(max_length=50)
    teacher_last_name=models.CharField(max_length=50)


class Student(models.Model):
    student_first_name = models.CharField(max_length=200)
    student_last_name = models.CharField(max_length=200)
    age = models.IntegerField(null=False, blank=False, default=0)
    roll_no = models.IntegerField(null=False, blank=False, default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

