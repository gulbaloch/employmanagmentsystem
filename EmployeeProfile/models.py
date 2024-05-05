from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)



class Designation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()



class JobDescription(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

   

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

  

class Employee(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    dateofjoining = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE)
    jobdescription = models.ForeignKey('JobDescription', on_delete=models.CASCADE)

   
