from django.shortcuts import render


def index(request):
    return render(request, "project0/project0index.html")


def name_1(request):
    return render(request, "project0/project0-name1.html")


def name_2(request):
    return render(request, "project0/project0-name2.html")


def name_3(request):
    return render(request, "project0/project0-name3.html")


def name_4(request):
    return render(request, "project0/project0-name4.html")
