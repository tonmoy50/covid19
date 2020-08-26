"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from homeapp import views as homeviews
from assessment import views as asses_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assessment_page', asses_views.assessment_page, name="assessment_page"),
    path('result/', asses_views.result, name="result"),
    path('home/', homeviews.index, name="home"),
    path('participants/', asses_views.participants, name="participants"),

    path('', include('homeapp.urls'), name="home"),   
    
    
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)