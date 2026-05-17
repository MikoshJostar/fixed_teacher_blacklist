from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})


@login_required
def add_student(request):

    # тільки адмін
    if not request.user.is_staff:
        return redirect('/admin/')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})