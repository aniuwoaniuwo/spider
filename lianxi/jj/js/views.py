from django.shortcuts import render
from django.http import HttpResponse
 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def index(request):
    return render(request, 'home.html')
def fff(request,c,d):
	if c>=d:
	    return HttpResponse(int(c))
		#return HttpResponse(str(c)
	else:
	    return HttpResponse(int(d))
		#return HttpResponse(str(d))
def home(request):
    #string = u"我在自强学堂学习Django，用它来建网站"
    #return render(request, 'home1.html', {'string': string})
	
	#sanguo=["魏国","蜀国","吴国"]
	#return render(request,'sanguo.html',{'sanguo':sanguo})
	#return render(request,'home.html')
	#list=map(str,range(100))
	#return render(request,'xunhuan.html',{'xunhuan':list})
	ruguo=445
	return render(request,'ruguo.html',{'ruguo':ruguo})
