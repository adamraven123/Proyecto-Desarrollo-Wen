from django.shortcuts import render

# Create your views here.
def index(request):
    data = {}
    template_name = 'index.html'
    return render(request,template_name,data)