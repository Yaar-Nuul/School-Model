
from django.db import models

class Classroom(models.Model):
  class_name= models.CharField(max_length=20)
  number_of_seats= models.IntegerField()
  number_of_students= models.IntegerField()
  class_teacher= models.CharField(max_length=20)
  courses= models.CharField(max_length=25)
  available_equipments= models.TextField()
  description = models.TextField()
def __str__(self):
  return f"{self.class_name}"









from django.db import models
from django.utils import timezone
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class ClassPeriod(models.Model):
    START_TIME = models.TimeField()
    END_TIME = models.TimeField()
    COURSE = models.ForeignKey('Course', on_delete=models.CASCADE)
    CLASSROOM = models.CharField(max_length=100)
    DAY_OF_WEEK = models.EnumChoiceField(enum=Weekday, default=Weekday.MONDAY)

    def __str__(self):
        return f"{self.CLASSROOM} - {self.DAY_OF_WEEK.name}"









