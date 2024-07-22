# from classroom.models import Class
# from django.db import models

# from course.models import Course

# class ClassPeriod(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
#     day_of_the_week = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from classroom.models import Class
from course.models import Course

class ClassPeriod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Add any other fields that exist in your database