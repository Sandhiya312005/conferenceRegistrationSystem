from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    address = models.TextField()
    country = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    paper_type = models.CharField(max_length=100)
    paper_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
