"""
URL configuration for Cheating_Detection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #! This will be the home route which will save the user detail
    path("detail/",views.Home),
    
    #! This route will capture the image of user for further comparision
    path("image/",views.Capture_Image),
    
    #! This route will start test
    path("test/",views.Test),
    
    path("cheat/",views.cheat)
]
