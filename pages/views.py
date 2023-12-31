from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1")


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'this_is_true': True,
        'my_number': 123,
        'my_list': [123, 42424, 13245643, 'ABC'],
        'my_html': '<h1>Hello World</h1>',
    }
    return render(request, 'about.html', my_context)
