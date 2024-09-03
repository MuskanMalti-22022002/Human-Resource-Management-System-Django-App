from rest_framework import serializers
from .models import Employee
from .models import Attendance
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'address', 'email', 'phone_number', 'designation']



class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'in_time', 'out_time']
        depth = 1 