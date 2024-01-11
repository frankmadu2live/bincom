from django.shortcuts import render
# from . import mydb_config
import sqlite3

# Create your views here.


def home(request):
    
    return render(request, 'bincompolls/home.html')