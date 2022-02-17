from django.shortcuts import render
from listings.models import Band
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html)')

def get_my_value(request, value):
    return HttpResponse('<p>Test<p>' + str(value))
    
def listing(request):
    return HttpResponse('<p>Test<p>' )

def contact_us(request):
    return HttpResponse('<p>Test<p>' )
