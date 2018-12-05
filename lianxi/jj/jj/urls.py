"""jj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from js import views as js_views
 
 
urlpatterns = [
    url(r'^$', js_views.home, name='home'),
	url(r'^add/$', js_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', js_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
	url(r'^max/(\d+)/(\d+)/$',js_views.fff,name='fff'),#5跟10比是5，原因？
	
	
	
]
