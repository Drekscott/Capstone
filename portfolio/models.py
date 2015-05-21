from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    class Meta:
        db_table = "clients"
        ordering = ['name']
    class Admin:
        pass

    def __unicode__(self):
        return self.name

class Medium(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table="media"
        verbose_name_plural="media"
        ordering=['name']

    class Admin:
        pass

    def __unicode__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=250)
    project_url=models.URLField('Project URL')
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    media = models.ManyToManyField(Medium)
    disciplines = models.CharField(max_length=200)
    completion_date = models.DateField()
    in_development=models.BooleanField()
    is_public = models.BooleanField(default=True)
    upvotes=models.IntegerField(default=0)
    thumbnail=models.FileField(upload_to='profile/%Y/%m/%d')

    class Meta:
        db_table = "projects"
        ordering = ['-completion_date']

    class Admin:
        pass

    def __unicode__(self):
        return self.name
