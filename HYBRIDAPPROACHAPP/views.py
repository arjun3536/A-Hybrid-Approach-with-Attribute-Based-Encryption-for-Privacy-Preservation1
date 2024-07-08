from django.shortcuts import render,redirect
from HYBRIDAPPROACHAPP.models import *
from datetime import datetime
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

def adminhome(request):
	return render(request,"abe/adminhome.html")
		
def operatorhome(request):
	return render(request,"abe/operatorhome.html")
		
def advocatehome(request):
	return render(request,"abe/advocatehome.html")

def adddata(request):
	msg=""
	if request.method=="POST":
		cd=CompanyData()
		userid=request.session["username"]
		cd.windturbine=encrypt(userid,request.POST["windturbine"])
		cd.steamproduction=encrypt(userid,request.POST["steamproduction"])
		cd.energyeffeciency=encrypt(userid,request.POST["energyeffeciency"])
		cd.synchronousmotors=encrypt(userid,request.POST["synchronousmotors"])
		cd.username_id=request.session["username"]
		cd.entrydate=datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')
		cd.save()
		msg="Data saved Successfully"
	return render(request,"abe/adddata.html",{"msg":msg})

def viewdata(request):
	mydata=""
	if request.method=="POST":
		wind=""
		steam=""
		motor=""
		energy=""
		username=""
		entrydate=""
		pid=request.POST["pid"]
		if CompanyData.objects.filter(id=pid).exists():
			request.session["pid"]=pid
			return redirect("decryptdata")
	if CompanyData.objects.all().exists():
		mydata=CompanyData.objects.all()
	return render(request,"abe/viewdata.html",{"mydata":mydata}) 

def decryptdata(request):
	mydata=""
	pid=request.session["pid"]
	wind=""
	steam=""
	motor=""
	energy=""
	username=""
	entrydate=""
	mydata=CompanyData.objects.filter(id=pid)
	for md in mydata:
		userid=md.username_id
		wind=decrypt(userid,md.windturbine)
		steam=decrypt(userid,md.steamproduction)
		energy=decrypt(userid,md.energyeffeciency)
		motor=decrypt(userid,md.synchronousmotors)
		username=md.username
		entrydate=md.entrydate
	return render(request,"abe/decryptdata.html",{"username":username,"entrydate":entrydate,"energy":energy,"motor":motor,"mydata":mydata,"userid":userid,"wind":wind,"steam":steam}) 



def loginpage(request):
	msg=""
	if request.method == "POST":
		usertype=request.POST.get("usertype","")
		username=request.POST.get("txtmobilenumber","")
		request.session["username"]=username
		password=request.POST.get("txtpassword","")
		if(usertype=="1" and username=="9876543210" and password=="9876543210"):
			return render(request,"abe/adminhome.html")
		elif(usertype=="2"):
			if operatorregister.objects.filter(mobilenumber=username,password=password).exists():
				dd=	operatorregister.objects.get(mobilenumber=username,password=password)
				if(dd.mobilenumber==username and dd.password==password):
					return render(request,"abe/operatorhome.html")
				else:
					msg="Invalid Mobilenumber or Password!"
			else:
				msg="Invalid Mobilenumber or Password!"

		elif(usertype=="3"):
			if UserRegister.objects.filter(mobilenumber=username,password=password).exists():
				dd=UserRegister.objects.get(mobilenumber=username,password=password)
				if(dd.mobilenumber==username and password==dd.password):
					return render(request, 'abe/advocatehome.html')
				else:
					msg="Invalid Mobilenumber or Password!"
			else:
				msg="Invalid Mobilenumber or Password!"
	return render(request,"abe/loginpage.html",{"msg":msg})
   				
def advocatecourtcasedisplay(request):
	if request.method=="POST":
		hid=request.POST.get("hid","")
		m=courtcase.objects.get(id=hid)
		dcaseid=m.caseid
		dcasetype=m.casetype
		dvictimside=decrypt(dcaseid+"22",m.victimside)
		daccuseside=decrypt(dcaseid+"22",m.accuseside)
		dcasedate=m.casedate
		return render(request,"abe/advocatecourtcasedisplaydec.html",{"dcaseid":dcaseid,"dcasetype":dcasetype,"dvictimside":dvictimside,"daccuseside":daccuseside,"dcasedate":dcasedate})
	else:	
		mydata=courtcase.objects.all()
		return render(request,"abe/advocatecourtcasedisplay.html",{"mydata":mydata})


def admincourtcasedisplay(request):
	mydata=courtcase.objects.all()
	return render(request,"abe/admincourtcasedisplay.html",{"mydata":mydata})

def operatorcourtcasedisplay(request):
	if request.method=="POST":
		hid=request.POST.get("hid","")
		m=courtcase.objects.get(id=hid)
		dcaseid=m.caseid
		dcasetype=m.casetype
		dvictimside=decrypt(dcaseid+"22",m.victimside)
		daccuseside=decrypt(dcaseid+"22",m.accuseside)
		dcasedate=m.casedate
		return render(request,"abe/operatorcourtcasedisplaydec.html",{"dcaseid":dcaseid,"dcasetype":dcasetype,"dvictimside":dvictimside,"daccuseside":daccuseside,"dcasedate":dcasedate})
	else:	
		mydata=courtcase.objects.all()
		return render(request,"abe/operatorcourtcasedisplay.html",{"mydata":mydata})

def  operatorregistercode(request):
	if request.method=="POST":
		obj=operatorregister()
		obj.firstname=request.POST.get("txtfirstname","")
		obj.lastname=request.POST.get("txtlastname","")
		obj.dob=request.POST.get("txtdob","")
		obj.gender=request.POST.get("gender","")
		obj.emailid=request.POST.get("txtemailid","")
		obj.password=request.POST.get("txtpassword","")
		obj.mobilenumber=request.POST.get("txtmobilenumber","")
		obj.save()                                                                 
		return render(request,"abe/operatorregister.html",{"msg":"Registered Successfully"})
	else:
		return render(request,"abe/operatorregister.html")


def operatordisplay(request):
	mydata=operatorregister.objects.all()
	return render(request,"abe/operatordisplay.html",{"mydata":mydata}) 

def  advocateregistercode(request):
	if request.method=="POST":
		obj=UserRegister()
		obj.firstname=request.POST.get("txtfirstname","")
		obj.lastname=request.POST.get("txtlastname","")
		obj.dob=request.POST.get("txtdob","")
		obj.gender=request.POST.get("gender","")
		obj.emailid=request.POST.get("txtemailid","")
		obj.password=request.POST.get("txtpassword","")
		obj.mobilenumber=request.POST.get("txtmobilenumber","")
		obj.save()                                                                 
	return render(request,"abe/UserRegister.html",{"msg":"Registered Successfully"})



def operatorviewdata(request):
	mydata=""
	if CompanyData.objects.all().exists():
		mydata=CompanyData.objects.all()
	return render(request,"abe/operatorviewdata.html",{"mydata":mydata}) 

def adminadvocatedisplay(request):
	mydata=UserRegister.objects.all()
	return render(request,"abe/adminadvocatedisplay.html",{"mydata":mydata}) 

def operatoradvocatedisplay(request):
	if request.method=="POST":
		aid=request.POST.get("aid","")
		s=UserRegister.objects.filter(id=aid)
		s.delete()
		mydata=UserRegister.objects.all()
		return render(request,"abe/operatoradvocatedisplay.html",{"mydata":mydata}) 
	else:
		mydata=UserRegister.objects.all()
		return render(request,"abe/operatoradvocatedisplay.html",{"mydata":mydata}) 


def  operatorcourtcasecode(request):
	if request.method=="POST":
		obj=courtcase()
		obj.caseid=request.POST.get("txtcaseid","")
		obj.casetype=request.POST.get("txtcasetype","")
		obj.victimside=encrypt(obj.caseid+"22",request.POST.get("txtvictimside",""))
		obj.accuseside=encrypt(obj.caseid+"22",request.POST.get("txtaccuseside",""))
		obj.casedate=request.POST.get("txtcasedate","")
		obj.save()
		return render(request,"abe/operatorcourtcasecode.html",{"msg":"Saved Successfully"})
	else:
		return render(request,"abe/operatorcourtcasecode.html")
