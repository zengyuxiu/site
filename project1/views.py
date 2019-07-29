

from django.shortcuts import render


def index(request):
    return render(request, "project1/project1index.html")

def name_1(request):
    return render(request, "project1/project1-name1.html")

def name_2(request):
    return render(request, "project1/project1-name2.html")

def name_3(request):
    return render(request, "project1/project1-name3.html")

def name_4(request):
    return render(request, "project1/project1-name4.html")

def name_5(request):
    return render(request, "project1/project1-name5.html")
