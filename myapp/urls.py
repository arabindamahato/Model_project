from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    
    path('',views.index, name='index'),
    path('/display',views.display, name='display'),
    path('/display-asc',views.display_asc, name='display_asc'),
    path('/display-specific',views.display_specific, name='display_specific'),
    path('/filter-data',views.filter_data, name='filter_data'),
    path('/like-data',views.like_data, name='like_data'),
    
]


