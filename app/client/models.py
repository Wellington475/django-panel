from django.db import models

class Client(models.Model):
	id_client = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	slug = models.SlugField(null = True)
	icon = models.CharField(max_length=155, null = True)
	keywords = models.CharField(max_length=155, null = True)
	author = models.CharField(max_length=155, null = True)
	description = models.CharField(max_length=155, null = True)
	color = models.CharField(max_length=155, null = True)
	image = models.CharField(max_length=155, null = True)
	
	def __unicode__(self):
		return client

class Login(models.Model):
	id_login = models.AutoField(primary_key=True)
	client = models.ForeignKey('Client')
	name = models.CharField(max_length=250)
	icon = models.CharField(max_length=250)