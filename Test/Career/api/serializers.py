from rest_framework import serializers

from Career.models import Category, Career


# class CareerSerializer(serializers.HyperlinkedModelSerializer):
# 	category_name = serializers.SlugRelatedField(queryset=Category.objects.all(),
# 	slug_field='name')

# 	class Meta:
# 		model = Career
# 		fields = [
# 			'title',
# 			'url',
# 			'slug',
# 			'category_name',
# 			'description',
# 		]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
	# url = serializers.HyperlinkedIdentityField(
	# view_name='categories',
	# lookup_field='slug'
	# )
	careers = serializers.HyperlinkedRelatedField(
	view_name='career-detail',
	# lookup_field='slug',
	many=True,
	read_only=True
	)
	class Meta:
		model = Category
		fields = [
			'url',
			'name',
			'slug',
			'overview',
			'careers'
		]

class CareerSerializer(serializers.HyperlinkedModelSerializer):
	category = serializers.SlugRelatedField(queryset=Category.objects.all(),
	slug_field='name')

	class Meta:
		model = Career
		fields = [
			'title',
			'url',
			'slug',
			'category',
			'description',
		]
