# from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Course_Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
    

class Course(models.Model):
    course=models.CharField(max_length=50)
    category=models.ForeignKey(Course_Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.course
    
class SubCourse(models.Model):
    course_title=models.CharField(max_length=50)
    main_course=models.ForeignKey(Course, on_delete=models.CASCADE)
    course_image=models.ImageField(upload_to='images/')
    course_desc=models.TextField(max_length=200)
    course_fee=models.IntegerField(default=0)
    def __str__(self):
        return self.course_title
    


# class Syllabus(models.Model):
#     course=models.ForeignKey(SubCourse, on_delete=models.CASCADE)
#     syllabus = ArrayField(
#        models.CharField(max_length=512)
#    )
    

    
    
    
