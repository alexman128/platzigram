from django.http import HttpResponse
import json
def hello_world(request):
    return HttpResponse('Hello world')

def sort_integers(request):
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = [int(x) for x in numbers]
    numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting"""
    if (age < 12):
        message = f"Sorry {name} you are not allowed"
    else:
        message = f"Welcome {name}"
    return HttpResponse(message)

