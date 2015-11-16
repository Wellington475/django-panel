# -*- coding: utf-8 -*-

from django.test import TestCase
from app.client.models import Client, Login

class ClientModelTestCase(TestCase):
	
	def setUp(self):
		client = Client()
		client.name = 'BigBoss'
		client.author = 'Test'
		client.keywords = 'test, test'
		client.save()