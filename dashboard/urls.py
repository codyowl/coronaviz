from django.urls import path,include,re_path
from dashboard import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('regions', views.regions_view, name='regions'),

]

