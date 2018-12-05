"""dj URL Configuration

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
from django.conf.urls import  url
from django.contrib import admin
from djdj import views as djdj_views

urlpatterns = [
    url(r'^djdj_home/$', djdj_views.index,name='home'),
    url(r'^djdj_columns/$', djdj_views.columns,name='columns'),
    url(r'^admin/', admin.site.urls),
    url(r'',djdj_views.index1,name='index1'),
]