from django.conf.urls import url
from django.views.generic import TemplateView

from Career.api.views import ( CategoryList, CategoryDetail, CareerList, 
	                          CareerDetail, ApiRoot)

urlpatterns = [
	url(r'^categories/$', CategoryList.as_view(), name=CategoryList.name),
	url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name=CategoryDetail.name),
	url(r'^careers/$', CareerList.as_view(), name=CareerList.name),
	url(r'^careers/(?P<pk>[0-9]+)/$', CareerDetail.as_view(), name=CareerDetail.name),
	url(r'^api/$', ApiRoot.as_view(), name=ApiRoot.name),
	url(r'^$', TemplateView.as_view(template_name="index.html"))
] 