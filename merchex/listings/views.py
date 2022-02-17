from django.shortcuts import render
from listings.models import Band
# Create your views here.

from django.http import HttpResponse

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

def get_my_value(request, value):
    return HttpResponse('<p>Test<p>' + str(value))
    
def listing(request):
    return HttpResponse('<p>Test<p>' )

def contact_us(request):
    return HttpResponse('<p>Test<p>' )
