from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    #return HttpResponse("<h1>Not Hello World</h1>")
    return render(request, "home.html", {})

def conact_view(request, *args, **kwargs):
    print(request)
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    print(request)
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 555, 6666, 9123, 123123, 312, "abc"]
    }
    return render(request, "about.html", my_context)