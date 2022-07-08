from django.db import models

# Create your models here.

class Slider(models.Model):
	DISCOUNT_DEAL = (
		('HOT DEALS','HOT DEALS'),
		('New Arraivels','New Arraivels'),

		)
	Image = models.ImageField(upload_to='media/slider_imgs')
	Discount_Deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
	SALE = models.IntegerField()
	Brand_Name = models.CharField(max_length=200)
	Discount = models.IntegerField()
	Link = models.CharField(max_length=200)

	def __str__(self):
		return self.Brand_Name


class Baner_area(models.Model):
	image = models.ImageField(upload_to='media/baner_imgs')
	Discount_Deal = models.CharField(max_length=100)
	SALE = models.IntegerField()
	Quotev = models.CharField(max_length=100)
	Discount = models.IntegerField()
	Link = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.image

class Main_Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Category(models.Model):
	main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name + '--' + self.main_category.name


class Sub_Category(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.category.main_category.name + "--" + self.category.name + "--" + self.name

