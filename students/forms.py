from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from students.models import Course, Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "phone",
            "courses"
        ]
    courses = ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=CheckboxSelectMultiple,
        required = False
    )   