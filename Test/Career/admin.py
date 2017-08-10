from django.contrib import admin

from .models import Category, Career


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fileds = ('name')
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)

class CareerAdmin(admin.ModelAdmin):
	list_display = ['title', 'category']
	search_fileds = ('title', 'category')
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Career

admin.site.register(Career, CareerAdmin)

