from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=100)
    users = models.ForeignKey(User,on_delete=models.CASCADE,related_name='categories')
    last_modified =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Url(models.Model):
    url=models.URLField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='urls')
    description =  models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        self.category.last_modified =timezone.now()
        self.category.save()

    def delete(self,*args,**kwargs):
        self.category.last_modified = timezone.now()
        self.category.save()
        super().delete(*args,**kwargs)











