
from django.db import models

class Course(models.Model):
    course= models.CharField(max_length=20)
    duration_of_course= models.DateField()
    number_of_students= models.IntegerField()
    number_of_courses = models.IntegerField()
    name_of_teachers=models.CharField(max_length=30)
    description_of_course=models.TextField(default=True)
def __str__(self):
        return f"{self.name_of_course} {self.duration_of_course}"






