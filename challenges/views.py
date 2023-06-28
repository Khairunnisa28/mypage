from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This works!")

def febuary(request):
    return HttpResponse("walk for at least 20 minutes every day!")