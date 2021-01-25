from django.db import models
import datetime as dt
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True)

    def save_profile(self):
        self.save()                   

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'  
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = CloudinaryField('images')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='Kenya')
        
    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects