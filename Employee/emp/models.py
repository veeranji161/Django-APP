from django.db import models

# Create your models here.
class Emp_Info(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.emp_name

