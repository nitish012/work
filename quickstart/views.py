from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializer,TeacherSerializer,StudentsSerializer
from rest_framework import generics
from .models import Student,Teacher


class StudentList(generics.ListAPIView):
    ''' fetching list of students'''
    queryset = Student.objects.all()
    serializer_class=StudentsSerializer
    #lookup_field = 'roll_no'

class InsertStudents(generics.CreateAPIView):
    ''' Inserting a records of students'''
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class InsertTeachers(generics.CreateAPIView):
    ''' Inserting a records of teachers'''
    queryset = Teacher.objects.all()
    serializer_class=TeacherSerializer

class StudentUpdate(generics.RetrieveUpdateAPIView):
    '''updating records of students'''
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    #lookup_field = 'roll_no'

class TeacherUpdate(generics.RetrieveUpdateAPIView):
    '''updating records of students'''
    queryset = Teacher.objects.all()
    serializer_class=TeacherSerializer    

