from django.shortcuts import render
from myapp.models import *


# Create your views here.

def index(request):
    return render(request, "index.html")

# Display all()
def display(request):
    data_topic = Topic.objects.all() # Topic is the Class name / Table name
    data_webpage = Webpage.objects.all() # Webpage is the Class name / Webpage name
    data_access_details = Access_Details.objects.all() # Access_Details is the Class name / Webpage name

    top = {'topics':data_topic, 'webpages':data_webpage, 'access_details':data_access_details}
    return render(request, "display.html", context=top)


# Display ascending order
def display_asc(request):
    access_details_asc = Access_Details.objects.order_by('date') # order_by() ordered all the data by asc order
    access_date = {'dates':access_details_asc}
    return render(request, "display_asc.html", context=access_date)


# Display a specific record # using get(key:value)
def display_specific(request):
    # webpage_details = Webpage.objects.get(:)    
    return render(request, "display_specific.html")  



# Display the filter data
def filter_data(request):
    filterdata = Webpage.objects.filter(top_name = "Music")
    return render(request, "filter_data.html", context={'webpage':filterdata}) 

#startswith , endswith, and contains check 
def like_data(request):
    return render(request, "like_data.html")