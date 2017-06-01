from django.shortcuts import render
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Printapp.models import UserProfile,StlFile,Model_project,Printer
from Printapp.forms import StlfileForm ,ModelfileForm#,Printer_Form
from django.contrib.auth.models import User

# Create your views here.
import os

def index(request):
	#os.system('python3 /home/mrzhou/Printer_v3/Printer/file/stl_file/stl_anylasis.py')
	return render(request,'index.html')

@csrf_exempt
def register(request):
	errors = []
	account = None
	password = None
	password2 = None
	email = None
	CompareFlag = False

	if request.method == 'POST':
		if not request.POST.get('account'):
			errors.append('account is empty')
		else:
			account = request.POST.get('account')

		if not request.POST.get('password'):
			errors.append('password is empty')
		else:
			password = request.POST.get('password')
		if not request.POST.get('password2'):
			errors.append('confirm password is empty')
		else:
			password2 = request.POST.get('password2')
		if not request.POST.get('email'):
			errors.append('email is empty')

		else:
			email = request.POST.get('email')
		
		if password is not None:
			if password == password2:
				CompareFlag = True
			else:
				errors.append('password and confirm password is not consistently')
			
		if account is not None and password is not None and password2 is not None and email is not None and CompareFlag :
			user = User.objects.create_user(account,email,password)
			user.save()

			userlogin = auth.authenticate(username = account,password = password)
			auth.login(request,userlogin)
			return HttpResponseRedirect('/index')
	return render(request,'register.html', {'errors': errors})

@csrf_exempt
def login(request):
	errors = []
	account = None
	password = None
	if request.method == 'POST':
		if not request.POST.get('account'):
			errors.append('account is empty')
		else:
			account = request.POST.get('account')

		if not request.POST.get('password'):
			errors.append('password is empty')
		else:
			password = request.POST.get('password')

		if account is not None and password is not None:
			user = auth.authenticate(username=account,password=password)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect('/index')
				else:
					errors.append('account error')
			else:
				errors.append('account or password error')

		return render(request,'login.html',{'errors':errors})
	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index')

@login_required
def dashboard(request):
	return render(request,'dashboard.html',{'user':request.user})


@login_required
def Stl_List(request):
	if request.method == 'POST':
		stl = StlfileForm(request.POST,request.FILES)
		if stl.is_valid():
			stl_file = stl.cleaned_data['stl_file']
			stl_name = str(stl_file)
			test = stl_name.split(".")
			if test[-1].lower() not in ['stl']:
				return HttpResponse("It's not stl file")
			else:
				Stl = StlFile()
				Stl.stl_name = stl_name
				Stl.stl_file = stl_file
				Stl.stl_owner = request.user
				Stl.save()
				Stl_i = StlFile.objects.get(stl_name = stl_name) 
				name = stl_name.split('.')[0]
				B_s = stl_name.split('.')[1]
				os.system('python3 /home/mrzhou/Printer_v3/Printer/file/stl_file/stl_anylasis.py '+name+' '+B_s)
				Stl_i.stl_image = 'stl_file/stl_image/'+name+'.png'
				Stl_i.save()
				
				stl = StlFile.objects.filter(stl_owner = request.user) 
				return render_to_response('dashboard.html',{'stl':stl,'user':request.user})

	else:
		stl = StlFile.objects.filter(stl_owner = request.user)
		return render_to_response('B_stl_list.html',{'stl':stl,'user':request.user})

@login_required
def Stl_Delete(request,pk):
	stl = StlFile.objects.get(pk=pk)
	path = "/home/mrzhou/Printer_v3/Printer/file/stl_file/%s"% (stl.stl_name)
	os.remove(path)
	stl.delete()
	return render_to_response('dashboard.html',{'user':request.user})


'''@login_required
def Stl_Pr_select(request,pk):
	import os 
	post = StlFile.objects.get(pk=pk)
	STLfile.append(post.stl_name)
	printer = Printer.objects.filter(pr_havier = request.user)
	return render_to_response('A_Printer_list.html',{'user':request.user,'post':post,'printer':printer})'''


@login_required
def  model_list(request):
	model_list = Model_project.objects.all()
	return render(request,'E_model_list.html',{'post':model_list,'user':request.user})

@login_required
def model_sell(request):
	if request.method == "POST":
		mf = ModelfileForm(request.POST,request.FILES)
		if mf.is_valid():
			proj = Model_project()
			proj.model_name = request.POST.get('model_name')
			proj.model_price = request.POST.get('model_price')
			proj.model_introd = request.POST.get('model_introd')
			proj.model_owner = request.user
			proj.model_image = mf.cleaned_data['model_image']
			proj.model_file = mf.cleaned_data['model_file']
			proj.save()

			return HttpResponseRedirect('/printer/model_list')
	else:	
		return render_to_response('E_model_sell.html',{'user':request.user})

@login_required
def model_owner(request):
	post = Model_project.objects.filter(model_owner=request.user)
	return render_to_response('E_model_owner.html',{'user':request.user,'post':post})

@login_required
def model_modify(request,pk):
	post = Model_project.objects.get(pk=pk)
	if request.method == 'POST':
		submit = request.POST.get('modify',None)
		if submit:
			post.model_name = request.POST['proj_name']
			post.model_price = request.POST['proj_name']
			post.model_introd = request.POST['proj_name']
			post.save()
			return HttpResponseRedirect('/dashboard')
		else:
			path = "/home/mrzhou/Printer_v3/Printer/file/%s"% (str(post.proj_image))
			path1 = "/home/mrzhou/Printer_v3/Printer/file/%s"% (str(post.proj_file))
			post.delete()
			os.remove(path)
			os.remove(path1)
			return render_to_response('dashboard.html',{'user':request.user})

	return render_to_response('E_model_modify.html',{'user':request.user,'post':post})


