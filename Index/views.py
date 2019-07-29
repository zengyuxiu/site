from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Index/index.html")

def charts(request):
    return render(request, "Index/charts.html")

def tables(request):
    return render(request, "Index/tables.html")

def DataIndex(request):
    return render(request, "Index/indexDATA.html")
