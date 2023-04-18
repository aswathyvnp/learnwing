from django.db import models
import datetime
# Create your models here.
from django.contrib.auth.models import User

from LearnwingApp.models import SubCourse


class OtherModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    dateOfBirth = models.DateField(default=datetime.date.today)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Addcart(models.Model):
    u_id=models.ForeignKey(User, on_delete=models.CASCADE)
    course_id=models.ForeignKey(SubCourse, on_delete=models.CASCADE)
    
