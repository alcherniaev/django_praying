from django.shortcuts import render

# Create your views here.
def praying(request):
    return render(request, "run_pray/pray.html")