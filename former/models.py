from django.db import models
from django.contrib.auth.models import User

from social_django.models import AbstractUserSocialAuth, UserSocialAuth, Nonce, Association, Code, DjangoStorage
# Create your models here.
class Forms(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank= True)
<<<<<<< HEAD
	p_id = models.CharField(max_length = 105,primary_key=True)
=======
	p_id = models.CharField(max_length = 110,primary_key=True)
>>>>>>> 04e0cae7ae216bf67beaeab93f0b8139758f3ed6
	form_name = models.CharField(max_length = 50,default='')
	description = models.CharField(max_length=1000,default='')
	def __str__(self):
		return str(self.p_id)

class question(models.Model):
	id = models.AutoField(primary_key = True)
	ques = models.CharField(max_length = 1000,default=' ')
	qtype = models.CharField(max_length =1, default=0)
	forms = models.ForeignKey(Forms,on_delete = models.CASCADE,null=True, blank=True)
	def __str__(self):
		return self.ques

class answer(models.Model):
	ans = models.CharField(max_length = 1000)
	question = models.ForeignKey(question,on_delete = models.CASCADE,null=True, blank=True)
	def __str__(self):
		return self.ans
