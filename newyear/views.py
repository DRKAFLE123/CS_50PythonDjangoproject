from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Welcome to NewYear App")

def index(request):
    now = datetime.datetime.now()
    current_date = datetime.date.today()
    context = {"newyear": now.month == 1 and  now.day == 1,"now":current_date}
    #c ontext dictionary is then passed to the template,
    return render(request, "newyear/index.html",context) 
#vwe can directly pass with curly-braces valuesnin place of context also




# import datetime
# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
