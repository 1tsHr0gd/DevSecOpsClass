import datetime

from django.utils import timezone
from django.db import models
from django import forms

# Create your models here.

class Project(models.Model):
	project_title = models.CharField(max_length = 50, default = 'Default')
	project_text = models.CharField(max_length = 500)
	start_date = models.DateTimeField('date started')

	def __str__(self):
		return self.project_text

	def was_created_recently(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days =1)

class Task(models.Model):
	assoc_project = models.ForeignKey(Project, default=1)
	task_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date created')

	def __str__(self):
		return self.task_text

	def getProjectTitle(self):
		return self.assoc_project.project_title

	def was_created_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days =1)

class Comment(models.Model):
	task = models.ForeignKey(Task)
	comment_text = models.CharField(max_length = 200)

	def __str__(self):
		return self.comment_text


class CommentForm(forms.Form):
	the_comment = forms.CharField(widget = forms.Textarea)

