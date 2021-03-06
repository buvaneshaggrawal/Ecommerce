from django.db import models

class Account(models.Model):
	user_id = models.IntegerField(default=0,unique=True,primary_key=True)
	user_name = models.CharField(max_length=20,unique=True)
	pwd = models.CharField(max_length=20)
	email = models.CharField(max_length=20,unique=True)
	acc_type = models.CharField(max_length=2,choices=(('CU','Customer'),('ME','Merchant')))
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=20,unique=True)
	def __unicode__(self):
		return self.user_name
"""class Account_view(models.Model):
        user_id = models.IntegerField(default=0,unique=True,primary_key=True)
	user_name = models.CharField(max_length=20,unique=True)
	phone = models.CharField(max_length=20,unique=True)
	def __unicode__(self):
		return self.user_name"""
        
class Customer(models.Model):
	account=models.ForeignKey(Account,unique=True)
	customer_id = models.IntegerField(default=0,unique=True,primary_key=True)
	customer_name= models.CharField(max_length=20)
	number= models.IntegerField(default=0)#no of orders
	balance= models.IntegerField(default=0)
	def __unicode__(self):
		return self.account.user_name

	
class Merchant(models.Model):
	account=models.ForeignKey(Account,unique=True)
	merchant_id =models.IntegerField(default=0,unique=True,primary_key=True)
	merchant_name=models.CharField(max_length=20)
	no_prod =models.IntegerField(default=0)
	rating =models.IntegerField(default=0)
	no_sold =models.IntegerField(default=0)
	def __unicode__(self):
		return self.account.user_name


class Product(models.Model):
	merchant=models.ForeignKey(Merchant)
	prod_id=models.IntegerField(default=0,unique=True,primary_key=True)
	prod_name=models.CharField(max_length=20)
	price=models.IntegerField(default=0)
	discount=models.IntegerField(default=0)
	number=models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.prod_id)


class Shipping_Company(models.Model):
	ship=models.IntegerField(default=0,unique=True,primary_key=True)
	ship_name=models.CharField(max_length=20)
	Address=models.CharField(max_length=20)
	phone=models.CharField(max_length=20,unique=True)
	no_sold=models.IntegerField(default=0)
	rating=models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.ship_name)


class Order(models.Model):
	order_id=models.IntegerField(default=0,unique=True,primary_key=True)
	customer=models.ForeignKey(Customer)
	total=models.IntegerField(default=0)
	taxes=models.IntegerField(default=0)
	discount=models.IntegerField(default=0)
	shipping=models.IntegerField(default=0)
	final_cost=models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.order_id)

class Product_Order(models.Model):
	order=models.ForeignKey(Order)
	product=models.ForeignKey(Product)
	quantity=models.IntegerField(default=1)	
	def __unicode__(self):
		return str(str(self.order)+" "+str(self.product))

class orderShip(models.Model):
	order=models.ForeignKey(Order)
	ship=models.ForeignKey(Shipping_Company)
	def __unicode__(self):
		return str(self.order)

class Transaction(models.Model):
	tid=models.IntegerField(default=0,unique=True,primary_key=True)
	customer=models.ForeignKey(Customer)
	merchant=models.ForeignKey(Merchant)
	order=models.ForeignKey(Order)
	def __unicode__(self):
		return str(self.tid)


