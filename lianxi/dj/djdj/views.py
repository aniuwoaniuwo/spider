from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'djdj/index.html')
def columns(request):
    return render(request,'columns.html')
def index1(request):
    return HttpResponse('fff')
