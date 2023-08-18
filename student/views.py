from django.shortcuts import render
from django.views import View
from .models import Student

class StudentView(View):
    template_name = 'student/student.html'

    def get(self, request):
        students = Student.objects.all()
        print(students)
        print(students.query)
        return render(request, self.template_name, {})