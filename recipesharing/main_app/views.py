from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello Cat Collector</h1>')
    return render(request, 'home.html')