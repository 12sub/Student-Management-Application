from django.urls import path
from .views import home_page, app_detail, app_students, app_update, app_delete, app_student_detail, app_students_update, app_student_delete, students_page, app_create

app_name = "apps"
urlpatterns = [
    path('', home_page, name='home'),
    path('<int:pk>/', app_detail, name='detail'),
    path('<int:pk>/update/', app_update, name='update'),
    path('<int:pk>/delete/', app_delete, name='delete'),
    path('create/', app_create, name='create'),
    path('student1/', students_page, name='stu'),
    path('student/', app_students, name='students'),
    path('students/<int:pk>', app_student_detail, name='student_detail'),
    path('students/<int:pk>/update', app_students_update, name='student_update'),
    path('students/<int:pk>/delete', app_student_delete, name='student_delete'),
]