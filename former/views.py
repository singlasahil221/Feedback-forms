from django.shortcuts import render,HttpResponse,Http404,redirect
from .models import Forms,question
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from random import choice
from string import ascii_letters
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.

@login_required(redirect_field_name='next',login_url='/login/')
def getQ(request):
	if request.user.is_authenticated:			
		pk,forms=0,[]
		a=User.objects.get(username=request.user)
		forms = a.forms_set.all()
		if request.method == "POST":
			a=Forms()
			a.user = User.objects.get(username = request.user)		
			k=0
			d=''.join(choice(ascii_letters) for i in range(100))
			while Forms.objects.filter(p_id = d).exists():
				d=uuid.uuid4().hex[:15]
			a.p_id = d
			a.form_name = request.POST.get('name').title()
			a.description = request.POST.get('Description')
			a.save()
			names=[] 
			names=request.POST.getlist("array[]") 
			opts=request.POST.getlist("opt[]") 
			for i in names:
				i=i.title()
				a.question_set.create(ques=i,qtype=opts[k])
				k+=1
				a.save()
			pk = a.p_id
			
		else:
			pass
		return render(request,'allin.html',{"pk": pk,'forms':forms})
	else:
		return redirect('/login/')

@login_required(redirect_field_name='next',login_url='/login/')
def postQ(request,pk):
	a = Forms.objects.get(p_id = pk)
	if a.user == request.user:
		quest=[]
		quest = a.question_set.all().order_by('id')
		return render(request,'all_reponses.html',{"form":a,"questions":quest})
	else:
		raise Http404('Not accessible.')



def getAns(request,pk):
	res=''
	if Forms.objects.filter(pk = pk).exists():
		a=Forms.objects.get(pk = pk)
		quest=a.question_set.all().order_by('id')
		if request.method == "POST":
			names=[]
			names=request.POST.getlist("array[]") 
			k=0
			for i in quest:
				i.answer_set.create(ans=names[k])
				k+=1
				i.save()
			pki = a.p_id
			res = "okk"
		else:
			pass
	else:
		return Http404("does not exists")
	return render(request,'fill-form.html',{"form_id": a.p_id,"name":a,"questions" : quest,"response":res})





@login_required(redirect_field_name='next',login_url='/login/')
def individual(request,pk , id):
	a = Forms.objects.get(p_id = pk)
	quest=[]
	quest = a.question_set.all()
	return render(request,"individual.html",{"questions":quest,"form_name":a.form_name,"id":id})


def logout_views(request):
	logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def create_user(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get('email', None)
		first_name = request.POST.get('first', None)
		last_name = request.POST.get('last', None)
		user, created = User.objects.get_or_create(username=username, email=email , first_name = first_name, last_name =  last_name)
		if created:
		    user.set_password(password) 
		    user.save()
		    return render(request,'log_reg.html',{'err':"success"})
		else :
			return render(request,'log_reg.html',{'err':"User already Exist!!"})
	else:
		return render(request,'log_reg.html',{'err': 'doesn\'t register'})