from django.db import models

class IPRipper(models.Model):
	ip = models.CharField(max_length=45)