from rest_framework import generics

from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import CategorySerializer, CareerSerializer
from Career.models import Category, Career


class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	name = 'category-detail'


class CareerList(generics.ListCreateAPIView):
	queryset = Career.objects.all()
	serializer_class = CareerSerializer
	name = 'career-list' 

class CareerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Career.objects.all()
	serializer_class = CareerSerializer
	name = 'career-detail' 

class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'categories': reverse(CategoryList.name, request=request),
			'careers': reverse(CareerList.name, request=request)
			})