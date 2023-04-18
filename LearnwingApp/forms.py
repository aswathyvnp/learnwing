
from django import forms

from .models import Course_Category,Course,SubCourse


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Course_Category
        fields='__all__'
        
class AddCourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        
class AddSubCourseForm(forms.ModelForm):
    class Meta:
        model=SubCourse
        fields='__all__'

# class SyllabusForm(forms.ModelForm):
#     class Meta:
#         model=Syllabus
#         fields='__all__'