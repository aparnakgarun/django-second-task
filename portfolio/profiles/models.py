

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    contact = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
