import sys, os

from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run, PIPE

def home(request):
    return render(request, 'scan/home.html')

def defaultscan(request):
    return render(request, 'scan/defaultscan.html')

def customports(request):
    return render(request, 'scan/customports.html')

def customcommand(request):
    return render(request, 'scan/customcommand.html')

def Startscan(request):
    return render(request, 'scan/startscan.html')

def external(request):
    inp = request.POST.get('parameter')

    # Take the input from the user and pass it to the script
    # The script will return the output
    # The output will be displayed on the webpage

    output = run([sys.executable, os.path.join(os.path.dirname(__file__), 'defaultscan.py'), inp,], stdout=PIPE).stdout.decode('utf-8')
    
    return render(request, 'scan/defaultscan.html', {'data1':output})


def custom(request):

    input1 = request.POST.get('parameter2')
    input2 = request.POST.get('parameter3')
    input3 = request.POST.get('parameter4')

    output = run([sys.executable, os.path.join(os.path.dirname(__file__), 'customIPandPort.py'), input1, input2, input3], stdout=PIPE).stdout.decode('utf-8')

    return render(request, 'scan/customports.html', {'data2':output})
