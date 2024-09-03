from django.db import models
from django.utils import timezone
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    email = models.EmailField(default='xyz@gmail.com')
    phone_number = models.CharField(max_length=15, default='')
   
# Attendance fields
    total_days_present = models.IntegerField(default=0)
    total_days_absent = models.IntegerField(default=0)
    daily_attendance = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name
#FOR DAILY ATTENDANCE IN AND OUT
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    in_time = models.TimeField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"