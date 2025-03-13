from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Course
from django.contrib import messages


def home(request):
    students = Student.objects.all()

    context = {
        'students':students,
        'range': range(50)
    }
    return render(request, "students/home.html", context)


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully")
            return redirect('/')
        else:
            messages.error(request, form.errors)
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, "students/register.html", context)



def details(request, id):
    student = Student.objects.prefetch_related('courses').get(id=id)
    form = StudentForm(instance=student)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True 
    context = {
        "student": student,
        "form":form
    }
    return render(request, "students/details.html", context)



    
def update(request, id):
    student = Student.objects.prefetch_related('courses').get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect('/')
        else:
            print("==================\n"*3)
            print(form.errors)
            print("==================\n"*3)
    else:
        form = StudentForm(instance=student)

    context = {'form': form}
    return render(request, "students/update.html", context)



def delete(request, id):
    student = Student.objects.prefetch_related('courses').get(id=id)
    student.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/')
