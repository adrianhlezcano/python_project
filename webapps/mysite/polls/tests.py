"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from polls.models import Poll

def create_poll(question, days):
  """
  Creates a poll with the given 'question' published the given number of 
  'days' offset to now (negatirve for polls published in  the pst,
  positive for polls that have yet to be published).
  """
  return Poll.objects.create(question=question,\
    pub_date=timezone.now()+datetime.timedelta(days=days))

class PollViewTests(TestCase):
  def test_index_with_no_poll(self):
    """
    If no polls exist, an appropiate message should be displayed.
    """
    response=self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'No polls are availables')
    self.assertQuerysetEqual(response.context['poll_list'], [])

  def test_index_with_a_past_poll(self):
    """
    If a past poll exist, it should be displayed on the index page.
    """
    create_poll(question='Past Poll', days=-1)
    response=self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['poll_list'], ['<Poll: Past Poll>'])

  def test_index_view_with_a_future_poll(self):
    """
    Polls with a pub_date in future should not be displayed on the
    index page.
    """
    create_poll(question='Future Poll', days=2)
    response=self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['poll_list'], [])

  def test_index_view_with_a_future_and_past_poll(self):
    """
    Even if both past and future polls exist, only past polls should be
    displayed.
    """
    create_poll(question='Past poll.', days=-30)
    create_poll(question='Future poll.', days=30)
    response=self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['poll_list'], ['<Poll: Past poll.>'])

  def test_index_view_with_two_past_polls(self):
    """
    The polls index page may display multiple polls.
    """
    create_poll(question='Past poll 1.', days=-30)
    create_poll(question='Past poll 2.', days=-39)
    response=self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['poll_list'],\
      ['<Poll: Past poll 1.>','<Poll: Past poll 2.>'])

class PollIndexDetailTest(TestCase):
  def test_detail_view_with_future_poll(self):
    """
    The detail view of a poll with a pub_date in the future should
    return a 404 not found. 
    """
    future_poll=create_poll(question='Future poll.', days=5)
    response=self.client.get(reverse('polls:detail', args=(future_poll.id,)))
    self.assertEqual(response.status_code, 404)

  def test_detail_view_with_past_poll(self):
    """
    The detail view of a poll with a pub_date in the past should
    display the poll's question
    """
    past_poll=create_poll(question='Past poll.', days=-2)
    response=self.client.get(reverse('polls:detail', args=(past_poll.id,)))
    self.assertContains(response, past_poll.question, status_code=200)


class PollMethodTest(TestCase):
  def test_was_published_today_with_future_poll(self):
    """
    was_published_today should return False for poll whose 
    pub_date is in the future.
    """
    future_poll=Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
    self.assertEqual(future_poll.was_published_today(), False)

  def test_was_published_today_with_old_poll(self):
    """
    was_published_today should return False for poll whose
    pub_date is older than today.
    """
    old_poll=Poll(pub_date=timezone.now()-datetime.timedelta(days=1))
    self.assertEqual(old_poll.was_published_today(), False)

  def test_was_published_today_with_recent_poll(self):
    """
    was_published_today should return True for poll whose
    pub_date are today.
    """
    recent_poll=Poll(pub_date=timezone.now()-datetime.timedelta(hours=1))
    self.assertEqual(recent_poll.was_published_today(), True)

