from django.db import models

class Teacher(models.Model):
   first_name= models.CharField(max_length=20)
   last_name= models.CharField(max_length=20)
   email= models.EmailField()
   code =models.PositiveSmallIntegerField()
   country = models.CharField(max_length= 20)
   gender =models.CharField(max_length=6)
   id_number = models.IntegerField()
   bio = models.TextField()
   status = models.BooleanField(default=False)
   place_of_work = models.CharField(max_length=35)
   salary_earned= models.IntegerField()
   level_of_education= models.CharField(max_length=30)
   def __str__(self):
       return f"{self.first_name} {self.last_name}"