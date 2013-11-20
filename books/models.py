from django.db import models

#cada model gera uma tabela;
#cada atributo no model corresponde a uma coluna daquela tabela;
#nome da cada atributo corresponde ao nome da coluna;
#e o tipo do campo (e.g. CharField) corresponde ao tipo da coluna (e.g. varchar)

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
