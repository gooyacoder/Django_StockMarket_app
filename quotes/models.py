from django.db import models

class Stock(models.Model):
	ticker = models.CharField(max_length=50)

	def __str__(self):
		return self.ticker
