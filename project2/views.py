from django.shortcuts import render


def index(request):
    return render(request, "project2/project2index.html")


def name_1(request):
    return render(request, "project2/project2-name1.html")


def name_2(request):
    return render(request, "project2/project2-name2.html")

