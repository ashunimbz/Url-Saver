from django.conf.urls import url,include
from authorize import views
app_name ='authorize'
urlpatterns = [
   url(r'^$',views.home ,name = 'home'),
   url(r'^add/(?P<cat_id>[0-9]+)/url',views.add_url,name = "add_url"),
   url(r'^add/category',views.add_category , name = "add_category"),
   url(r'^(?P<cat_id>[0-9]+)/urls$',views.show_urls , name = "show_urls"),
]