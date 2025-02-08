from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year=models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Tool(models.Model):
    name = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='tools_logos/', blank=True, null=True)
    def __str__(self):
        return self.name

