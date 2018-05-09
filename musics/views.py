from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime

# Create your views here.
def hello_view(request):
    current_time: object = datetime.datetime.now()

    return render(request, 'hello_django.html', {
        'data': "Hello Django",
        'mytime': current_time
    })