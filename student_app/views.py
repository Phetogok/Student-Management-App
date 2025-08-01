from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import StudentForm
from .models import Students

# Creat View
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('students')
    
    else:
        form = StudentForm()
    
    return render(request, 'create.html', {'form':form})

# Get View
def get_student(request):
    student = Students.objects.all()
    return render(request, 'home.html', {'students': student})

# Update View
def update_student(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'update.html', {'form':form})


# Delete View
def delete_student(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')