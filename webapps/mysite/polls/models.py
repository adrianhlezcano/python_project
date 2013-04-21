from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
  question=models.CharField(max_length=200)
  pub_date=models.DateTimeField('date_published')

  def __unicode__(self):
    return self.question

  def was_published_today(self):
    now=timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date < now

  was_published_today.admin_order_field='pub_date'
  was_published_today.boolean=True
  was_published_today.short_description='Published today?'

class Choice(models.Model):
  poll=models.ForeignKey(Poll)
  choice_text=models.CharField(max_length=200)
  votes=models.IntegerField(default=0)

  def __unicode__(self):
    return "{0}: {1}".format(self.choice_text, self.votes)
