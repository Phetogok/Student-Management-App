from django.db import models

# Create your models here.
class Students(models.Model):
    student_num = models.IntegerField(max_length=10)
    student_firstname = models.CharField(max_length=100)
    student_lastname = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_course = models.CharField(max_length=100)

    def __str__(self):
        return self.student_firstname
