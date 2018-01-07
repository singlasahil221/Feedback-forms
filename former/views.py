from django.shortcuts import render,HttpResponse,Http404,redirect
from .models import Forms,question
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from random import choice
from string import ascii_letters
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request,'home1.html',{'user':request.user,'request':request})
@login_required(login_url='/login/')
def getQ(request):
	if request.user.is_authenticated:			
		pk=0
		if request.method == "POST":
			a=Forms()
			a.user = User.objects.get(username = request.user)		
			k=0
			d=''.join(choice(ascii_letters) for i in range(100))
			while Forms.objects.filter(p_id = d).exists():
				d=uuid.uuid4().hex[:15]
			a.p_id = d
			a.form_name = request.POST.get('name')
			a.description = request.POST.get('Description')
			a.save()
			names=[] 
			names=request.POST.getlist("array[]") 
			opts=request.POST.getlist("opt[]") 
			for i in names:
				a.question_set.create(ques=i,qtype=opts[k])
				k+=1
				a.save()
			pk = a.p_id
		else:
			pass
		return render(request,'index.html',{"pk": pk})
	else:
		return redirect('/login/')

def getAns(request,pk):
	res=''
	if Forms.objects.filter(pk = pk).exists():
		a=Forms.objects.get(pk = pk)
		quest=a.question_set.all()
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
	return render(request,'ques.html',{"form_id": a.p_id,"name":a,"questions" : quest,"response":res})

@login_required(login_url='/login/')
def postQ(request,pk):
	a = Forms.objects.get(p_id = pk)
	quest=[]
	quest = a.question_set.all()
	return render(request,'admin.html',{"form":a.form_name,"questions":quest})

@login_required(login_url='/login/')
def all_forms(request):
	a=User.objects.get(username=request.user)
	forms=[]
	forms = a.forms_set.all()
	return render(request,'all_forms.html',{'forms':forms})

@login_required(login_url='/login/')
def individual(request,pk , id):
	a = Forms.objects.get(p_id = pk)
	quest=[]
	quest = a.question_set.all()
	return render(request,"individual.html",{"questions":quest,"form_name":a.form_name,"id":id})

def login_view(request):
	if request.method=='POST':
		username=request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if username and password:
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
				redirect('/')
			else:
				return render(request,'log_reg.html',{'err':'Incorrect Username/Password!!','user':request.user,'request':request})
		else:
			return render(request,'log_reg.html',{'err':'Enter Username/Password correctly!!','user':request.user,'request':request})
	elif request.method == 'GET':
		if request.user.is_authenticated :
			if request.user.is_superuser :
				return redirect('/')
			return redirect('/')
		return render(request,'log_reg.html',{'user':request.user,'request':request})
	return redirect('/')

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