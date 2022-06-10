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