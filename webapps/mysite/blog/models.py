from django.db import models
import datetime

# Create your models here.
class BlogPost(models.Model):
  title=models.CharField(max_length=150)
  body=models.TextField()
  timestamp=models.DateTimeField()

  def __unicode__(self):
    return self.title

  def was_published_today(self):
    tomorrow=datetime.datetime.now()+datetime.timedelta(days=1)
    yesterday=datetime.datetime.now()-datetime.timedelta(days=1)
    return yesterday <= self.timestamp < tomorrow
