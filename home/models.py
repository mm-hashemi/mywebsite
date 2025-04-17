from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)  # Store icon class or path

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_url = models.URLField()
    code_url = models.URLField()

    def __str__(self):
        return self.title