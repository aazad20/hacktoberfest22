from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=40)
    stupass = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.stuname

        "https://docs.google.com/document/d/1rU34Egir35aiqvncCVnv2zQjHHl_4ccamdXpn8_U3Lo/edit"

