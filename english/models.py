from django.db import models

class Word(models.Model):
	into_english = models.CharField(max_length=200)
	into_russian = models.CharField(max_length=200)

	def __str__(self):
		return self.into_english
