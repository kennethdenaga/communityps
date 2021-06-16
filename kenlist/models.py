from django.db import models


class Donator(models.Model):
	name = models.TextField(max_length=50)
	contactnumber = models.CharField(max_length=11)
	eadd = models.TextField(default='')

	def __str__(self):
		return self.name

class Donation(models.Model):
	donation = models.TextField(max_length=50)
	donation_type = models.CharField(max_length=50, default='')
	donator = models.ForeignKey(Donator, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Recipient(models.Model):
    recname = models.DateField(max_length=50)
    rec_contactnumber=models.TextField(max_length=11)
    donation = models.ForeignKey(Donation, default=None, on_delete=models.CASCADE)

    def __str__(self):
    	return self.name


class Location(models.Model):
    date = models.DateField(max_length=50)
    location = models.TextField(max_length=50)
    donation = models.ForeignKey(Donation, default=None, on_delete=models.CASCADE)

    def __str__(self):
    	return self.name


class Remarks(models.Model):
	status=models.TextField(max_length=50,default='')
	remarks= models.TextField(max_length=50,default='')
	donation = models.ForeignKey(Donation, default=None, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
