from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

def ajax_list(request):
    a=range(100)
    return JsonResponse(a, safe=False)
def ajax_dict(request):
    name_dict={'twz':'aaa','mz':'bbb'}
    return JsonResponse(name_dict)
