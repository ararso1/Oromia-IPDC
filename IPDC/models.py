from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Investor(models.Model):
	choices=(
		('Mr.','Mr.'),
		('Mrs.','Mrs.'),
		('Ms.','Ms.'),
		('Mx.','Mx.'),
		('Miss','Miss'),
		('Dr.','Dr.'),
		('Prof.','Prof.')
		)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=300,choices=choices,default=1)
	first_name=models.CharField(max_length=300)
	middle_name=models.CharField(max_length=300)
	last_name=models.CharField(max_length=300)
	gender=models.CharField(max_length=300)
	email=models.EmailField(max_length=300)
	phonenumber=models.CharField(max_length=300)
	education_level=models.CharField(max_length=300)
	current_Address=models.CharField(max_length=300)
	Tin=models.CharField(max_length=300)
	passport=models.FileField(null=True,blank=True)
	id_card=models.FileField(null=True,blank=True)

	def __str__(self):
		return self.title + self.first_name

class DomesticRequest(models.Model):
	types=(
		('License','License'),
		('Land Request','Land Request'),
		('Expansion','Expansion'),
		)
	sectors=(
		('Manufacturing','Manufacturing'),
		('Agriculture','Agriculture'),
		('Service','Service'),
		)
	formchoice=(
		('soleprorietor','soleprorietor'),
		('PLC','PLC'),
		('joint-venture','joint-venture')
		)
	status=(
		('onlist','onlist'),
		('pending','pending'),
		('approved','approved'),
		('denied','denied'),
		)
	investor=models.ForeignKey(Investor,on_delete=models.CASCADE)
	form_of_investment=models.CharField(max_length=300,choices=formchoice)
	requested_type=models.CharField(max_length=300,choices=types)
	requested_land=models.FloatField()
	sector=models.CharField(max_length=300,choices=sectors)
	project_name=models.CharField(max_length=300)
	project_description=models.TextField(max_length=300)
	capital=models.FloatField()
	owner_equity=models.FloatField()
	bank_loan=models.FloatField()
	temporay_job=models.CharField(max_length=300)
	Permanent_job=models.CharField(max_length=300)
	proposal=models.FileField(null=True,blank=True)
	bank_statement=models.FileField(null=True,blank=True)
	date=models.DateField(auto_now_add=True)
	primary_checked=models.BooleanField(default=False)
	secondary_checked=models.BooleanField(default=False)
	tertiary_checked=models.BooleanField(default=False)
	status=models.CharField(max_length=300,choices=status,default='onlist',blank=True )
	def __str__(self):
		return self.form_of_investment
	


class Privatechat(models.Model):
	primary_user=models.ForeignKey(User,on_delete=models.CASCADE)
	secondary_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='private')
	class Meta:
		unique_together = ["primary_user", "secondary_user"]
	def __str__(self):
		return self.primary_user.username +" " + self.secondary_user.username
class Message(models.Model):
	privatechat = models.ForeignKey(Privatechat,on_delete=models.CASCADE)
	msg = models.TextField(max_length=1000000)
	image=models.ImageField(null=True,blank=True)
	filee=models.FileField(null=True,blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	written_by = models.ForeignKey(User,on_delete=models.CASCADE)
	seen=models.BooleanField(default=False)
	def __str__(self):
		return str(self.privatechat)
class Notification(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	note_text=models.TextField(max_length=3000)
	seen=models.BooleanField(default=False)
	link=models.URLField(max_length = 200,null=True,blank=True)
	def __str__(self):
		return str(self.note_text[:30] +' ...')


class FeedBack(models.Model):
		feeder=models.ForeignKey(User,on_delete=models.CASCADE)
		domesticrequest=models.ForeignKey(DomesticRequest,on_delete=models.CASCADE)
		feedback_text=RichTextField(null=True,blank=True)
		allow_investor_to_see=models.BooleanField(default=True)
		def __str__(self):
			return str(self.feeder) + '____' + str(self.domesticrequest)

class RichText(models.Model):
	mytext=RichTextField(null=True,blank=True)

class Parksite(models.Model):
    name=models.CharField(max_length=300)
    site_manager=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Department(models.Model):
    parksite=models.ForeignKey(Parksite,on_delete=models.CASCADE)
    department_name=models.CharField(max_length=300)
    dept_manager=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.department_name

class Case(models.Model):
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    case_title = models.CharField(max_length=300)
    case_txt=RichTextField(null=True,blank=True)
    files=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.case_title

