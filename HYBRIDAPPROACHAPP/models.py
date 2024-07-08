from django.db import models

class courtcase(models.Model):
	caseid=models.CharField(max_length=200,default='')
	casetype=models.CharField(max_length=200,default='')
	victimside=models.CharField(max_length=200,default='')
	accuseside=models.CharField(max_length=200,default='')
	casedate=models.CharField(max_length=200,default='')

class operatorregister(models.Model):
	firstname=models.CharField(max_length=200,default='')
	lastname=models.CharField(max_length=200,default='')
	gender=models.CharField(max_length=200,default='')
	dob=models.CharField(max_length=200,default='')
	emailid=models.CharField(max_length=200,default='')
	password=models.CharField(max_length=200,default='')
	mobilenumber=models.CharField(max_length=200,default='')



class UserRegister(models.Model):
	firstname=models.CharField(max_length=200,default='')
	lastname=models.CharField(max_length=200,default='')
	gender=models.CharField(max_length=200,default='')
	dob=models.CharField(max_length=200,default='')
	emailid=models.CharField(max_length=200,default='')
	password=models.CharField(max_length=200,default='')
	mobilenumber=models.CharField(max_length=200,primary_key=True)


class CompanyData(models.Model):
	windturbine=models.CharField(max_length=500,default='')
	steamproduction=models.CharField(max_length=500,default='')
	energyeffeciency=models.CharField(max_length=500,default='')
	synchronousmotors=models.CharField(max_length=500,default='')
	entrydate=models.CharField(max_length=500,default='')
	username=models.ForeignKey(UserRegister,on_delete=models.PROTECT)

