from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.
def index():
    #return render(request,'index.html')
    return HttpResponse('1')
def home(request):
    list=['自强学堂','渲染json到模板']
    dict={'site':'自强学堂','author':'涂伟忠'}
    return render(requesr,'home.html',{
        'list':json.dumps(list),
        'dict':json.sumps(dict)
    })