import os, django, sys
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE','cookit.settings')
django.setup()

from products.models import Product, Type, Taste, ProductTaste, Image, Description, Event

def product_db():

	CSV_PATH_PRODUCTS = './products.csv'
	with open(CSV_PATH_PRODUCTS) as csv_file:
		rows = csv.reader(csv_file,delimiter=',')
		next(rows,None)
		for row in rows:
			if row[0] : 
				type_name = row[0]
				Type.objects.create(name=type_name)
			
			product_name = row[1]
			taste_name = row[2]
			cooking_time = row[3]
			price = row[4]
			sales = row[5]
			stock = row[6]
			image_url = row[7]
			sub_name = row[8]
			description_image_url = row[9]
			limited = row[10]
			new = row[11]
			description_text = row[12]

			type = Type.objects.get(name=type_name)
			Product.objects.create(
				name = product_name,
				cooking_time = cooking_time,
				price = price,
				sales = sales,
				stock = stock,
				sub_name = sub_name,
				type = type
				)

			product = Product.objects.get(name=product_name)

			Event.objects.create(
				limited = limited,
				new = new,
				product=product
				)
			
			Image.objects.create(
				image_url = image_url,
				product_id = product.id)

			Description.objects.create(
				image_url = description_image_url,
				text = description_text,
				product = product)

				
			Taste.objects.get_or_create(name=taste_name)
			taste = Taste.objects.get(name=taste_name)
			
			product.producttaste_set.create(
				taste=taste)
			
product_db()
