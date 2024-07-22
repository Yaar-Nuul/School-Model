# from rest_framework import generics
# # from .models import Course
# from .serializers import CourseSerializer
# from .permissions import CustomPermission  




# from rest_framework.response import Response
# from rest_framework.views import APIView
# from student.models import Student
# from .serializers import StudentSerializer
# from teacher.models import Teacher
# from .serializers import TeacherSerializer
# from classperiod.models import ClassPeriod
# from .serializers import ClassPeriodSerializer
# from course.models import Course
# from .serializers import CourseSerializer
# from rest_framework import status


# class ClassListView(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
    
# class TeacherListView(APIView):
#     def get(self, request):
#         Teachers = Teacher.object.all()
#         serializer = TeacherSerializer(Teachers, one=True)
#         return Response(serializer.data)
    
# class ClassPeriodListView(APIView):
#     def get(self, request):
#         ClassPeriods = ClassPeriod.cbject.all()
#         serializer = ClassPeriodSerializer(ClassPeriods, many=True)
#         return Response(serializer.data)
    
# class CourseListView(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = StudentSerializer( data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=
#                             status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=
#                             status.HTTP_400_BAD_REQUEST)
# class StudentListView(APIView):
#     def get(self, request):
#         Students = Student.object.all()
#         serializer = StudentSerializer(Students, many=True)
#         return Response(serializer.data)

#     def post(self, request, id):
#         serializer = CourseSerializer( data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=
#                             status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=
#                             status.HTTP_400_BAD_REQUEST)
        
    
# class StudentDetailView(APIView):

#     def get(self, request, id):
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
   
#     def put(self, request,id):
#         student = Student.objects.get(id =id)
#         serializer = StudentSerializer( student)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



#     def delete(self, request, id):
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response(
#             status=status.HTTP_202_ACCEPTED
#         )




# class CourseListView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [CustomPermission]  




from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from classroom.models import Class
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from course.models import Course
from .serializers import StudentSerializer, TeacherSerializer, ClassPeriodSerializer, CourseSerializer
from .permissions import CustomPermission
from rest_framework import generics

class ClassListView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassPeriodSerializer
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get_object(self, id):
        try:
            return Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)