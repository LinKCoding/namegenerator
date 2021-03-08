from django.shortcuts import render

from .models import FullName

def index(request):
    all_names_list = FullName.objects.all()
    context = { "all_names_list" : all_names_list }
    return render(request, "djname/index.html", context)