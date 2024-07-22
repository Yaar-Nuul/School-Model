
from django.db import models
from classroom.models import Class
from course.models import Course

from django.db.models import ExpressionWrapper, DateTimeField
from django.db.models.functions import Now



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



current_date_expr = ExpressionWrapper(
    Now(),
    output_field=DateTimeField()
)
results = ClassPeriod.objects.annotate(current_date=current_date_expr).filter(current_date__gte=F('timestamp_column'))