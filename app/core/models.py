from django.db import models

class Application(models.Model):
	id_application = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	icon = models.CharField(max_length=155)
	color = models.CharField(max_length=155)
	
	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return name

	class Meta:
		db_table = "application"