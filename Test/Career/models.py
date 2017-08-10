from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=80)
	slug = models.SlugField()
	overview = models.TextField()


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"


class Career(models.Model):
	title = models.CharField(max_length=80)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index = True, related_name="careers")
	slug = models.SlugField()
	description = models.TextField()


	def __str__(self):
		return self.title