"""lr_1_FirstStepWithDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from app1.views import index, summary_w, index_no_creative, summary_w_no_creative
from bank import views 

urlpatterns = [
	re_path(r'^/summary', index),
	re_path(r'^/summary_2', summary_w),
    re_path(r'^/summary_no_creative', index_no_creative),
    re_path(r'^/summary_2_no_creative', summary_w_no_creative),
	re_path(r'^bank', views.index),
    path('admin/', admin.site.urls),
    re_path(r'^', index)
]
