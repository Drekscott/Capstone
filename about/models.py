from django.db import models

 # Create your models here.
class About(models.Model):
    title = models.CharField(max_length = 30)
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    content=models.TextField()
    school=models.CharField(max_length=200)
    school_year=models.IntegerField()
    pub_date=models.DateTimeField('Date published')
    enable_comments=models.BooleanField(default=True)
    class Meta:
        db_table = "about"

    class Admin:
        pass

    def __unicode__(self):
        return self.title
