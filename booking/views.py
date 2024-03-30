from django.shortcuts import render
from booking.models import Room, Booking
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Some message :", status=400)
    context = {
        "render_string": "Hello, world!"
    }
    return render(request, template_name="booking/index.html", context=context)