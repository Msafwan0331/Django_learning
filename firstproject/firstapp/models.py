from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    STUDENT_DOMAIN = [
        ("BSCS", "COMPUTER SCIENCE"),
        ("BSIT", "INFORMATION TECHNOLOGY"),
        ("BSSE", "SOFTWARE ENGEERENING"),
        ("BSDS", "DATA SCIENCE"),
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rollno = models.SmallIntegerField
    image = models.ImageField(upload_to="students/")
    type = models.CharField(max_length=4, choices=STUDENT_DOMAIN)

    def __str__(self):
        return self.name


class StdSubjects(models.Model):
    SUBJECTS = [
        ("PF", "Programming"),
        ("OOP", "Object oriented programming"),
        ("DSA", "Data structures"),
        ("DAA", "Analysis of algo"),
    ]
    CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    ]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="Subject"
    )
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=4, choices=SUBJECTS)
    grade = models.CharField(max_length=4, choices=CHOICES)

    def __str__(self):
        return f"{self.subject} added for {self.student.name}"





     
