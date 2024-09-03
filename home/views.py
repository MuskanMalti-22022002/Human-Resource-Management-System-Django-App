from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from home.models import Employee
from .models import Attendance, Employee
from .serializers import AttendanceSerializer
from django.shortcuts import render, get_object_or_404
from .models import Employee, Attendance
from django.db.models import Count
from .models import Employee



# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")

def attendance(request):
    return render(request,"attendance.html")

def report(request):
    return render(request,"report.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=contact(name=name, email=email ,phone=phone)
        contact.save() 
    return  render(request,"contact.html")


    
#API TO ADD A NEW EMPLOYEE
@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API FOR RETRIEVE THE LIST OF ALL EMPLOYEES
@api_view(['GET'])
def get_all_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
from django.shortcuts import render
from .models import Employee

def home(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'index.html', {'employees': employees})


@api_view(['POST'])
def mark_attendance(request):
    try:
        employee_id = request.data.get('employee_id')
        date = request.data.get('date')
        in_time = request.data.get('in_time')
        out_time = request.data.get('out_time')

        # Find or create attendance record for the given date and employee
        employee = Employee.objects.get(id=employee_id)
        attendance, created = Attendance.objects.get_or_create(employee=employee, date=date)

        # Update in_time or out_time if provided
        if in_time:
            attendance.in_time = in_time
        if out_time:
            attendance.out_time = out_time

        attendance.save()
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#TO RETREIVE ATTENDANCE DETAIL OF A PARTICULAR EMPLOYEE    
@api_view(['GET'])
def get_attendance(request, employee_id):
    try:
        # Get the employee instance
        employee = Employee.objects.get(id=employee_id)
        
        # Retrieve all attendance records for the given employee
        attendance_records = Attendance.objects.filter(employee=employee)
        
        # Serialize the attendance records
        serializer = AttendanceSerializer(attendance_records, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
def employee_detail(request, employee_id):
    # Fetch the employee object
    employee = get_object_or_404(Employee, id=employee_id)
    
    # Fetch the attendance records for the employee
    attendance_records = Attendance.objects.filter(employee=employee)
    
    # Pass the employee and attendance records to the template
    return render(request, 'employee_detail.html', {
        'employee': employee,
        'attendance_records': attendance_records,
    })
    
def department_report(request):
    # Query the database to count the number of employees in each department
    report = Employee.objects.values('department').annotate(employee_count=Count('id'))

    # Pass the report data to the template
    return render(request, 'department_report.html', {
        'report': report,
    })