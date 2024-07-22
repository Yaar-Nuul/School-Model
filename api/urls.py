from django.urls import path
from .views import ClassPeriodListView, StudentListView
from .views import TeacherListView
from .views import ClassListView
from .views import CourseListView

urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    path("teachers/",TeacherListView.as_view(),name="teachers_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("classperiod/",ClassPeriodListView.as_view(),name="classperiod_list_view"),
    path("class/",ClassListView.as_view(),name="class_list_view"),
    path("student/<int:id>/", StudentListView.as_view(), name="student_detail_view"),
    # path("")
]






