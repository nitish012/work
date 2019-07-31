from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student,Teacher



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_first_name','teacher_last_name')


class StudentsSerializer(serializers.ModelSerializer):
    ''' read only'''
    teacher = TeacherSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ('student_first_name','student_last_name','age','roll_no','teacher')


class StudentSerializer(serializers.ModelSerializer):
    ''' writting data'''
    teacher = TeacherSerializer()

    # def create(self, validated_data):
    #     teacher_serializer = TeacherSerializer(validated_data.get('teacher'))
    #     teacher_serializer.save()
    #     return Student.objects.create(**validated_data)

    class Meta:
        model = Student
        fields = ('student_first_name','student_last_name','age','roll_no','teacher')

    
    # def create(self, validated_data):
    #     teachers_data = validated_data.pop('teacher')
    #     data = Student.objects.create(**validated_data)
    #     for teacher_data in teachers_data:
    #         Teacher.objects.create(teacher_first_name = data, **teacher_data)
    #     return data

    def create(self, validated_data):
        teachers_data = validated_data.pop('teacher')
        data = Student.objects.create(**validated_data)
        Teacher.objects.create(teachers_data=data, **teachers_data)
        return data 

    def update(self, instance, validated_data):
        teachers_data = validated_data.pop('teacher')
        teachers = Teacher.objects.filter(teacher_first_name="xyz")
        instance.save() 
        
        for teacher_data in teachers_data:
            teacher =  teachers.pop(0)
            teacher.teacher_first_name = teacher_data.get('teacher_first_name', teacher.teacher_first_name)
            teacher.save()
        return instance



    