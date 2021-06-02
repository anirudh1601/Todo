from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	task = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.task + ' | ' + str(self.completed) + ' | ' + str(self.date_posted)

	def get_absolute_url(self):
		return reverse('posted')


class City(models.Model):
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'cities'

