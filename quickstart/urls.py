from django.urls import path
from .views import InsertStudents,InsertTeachers,StudentList,StudentUpdate,TeacherUpdate


urlpatterns=[
    path('students/',StudentList.as_view()),
    path('students/<int:pk>/',StudentUpdate.as_view()),
    path('teachers/<int:pk>/',TeacherUpdate.as_view()),
    path('students/insert/',InsertStudents.as_view()),
    path('teachers/insert/',InsertTeachers.as_view()),
    
]