
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Привет! с вами говорит Джанго-релизнутый</h1>")
