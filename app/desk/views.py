# -*- coding: utf-8 -*-

from django.shortcuts import render
from app.core.models import Application

def home(request):
	apps = Application.objects.all()
	context = {
		"apps": apps
	}
	return render(request, "desk/index.html", context)