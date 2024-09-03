from django.contrib import admin
from django.urls import path
from home import views
from .views import mark_attendance
from .views import get_attendance
from django.urls import path
from .views import employee_detail
from .views import department_report



urlpatterns = [
    path('',views.index,name="home"),
    path('attendance',views.attendance,name="attendance"),
    path('report',views.report,name="report"),
    path('contact',views.contact,name="contact"),
    path('add-employee/', views.add_employee, name='add-employee'),
    path('employees/', views.get_all_employees, name='get-all-employees'),
    path('api/attendance/', mark_attendance, name='mark_attendance'),
    path('api/attendance/<int:employee_id>/', get_attendance, name='get_attendance'),
    path('employee/<int:employee_id>/', employee_detail, name='employee_detail'),
    path('report/departments/', department_report, name='department_report')
]