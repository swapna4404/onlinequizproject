from django.shortcuts import render
from django.http import HttpResponse
from C_programming.models import Quiz
from Django.models import Typeform
from Java.models import FlashcardSet
from Python.models import Form
from cpp.models import cppform
from DSA.models import Dsaform


def index(request):
    return render(request, 'index.html')

def C_programming(request):
    return render(request, 'C_programming.html')

def Django(request):
    return render(request, 'Django.html')

def Python(request):
    return render(request, 'Python.html')

def Java(request):
    return render(request, 'Java.html')
def cpp(request):
    return render(request, 'cpp.html')
def DSA(request):
    return render(request, 'DSA.html')