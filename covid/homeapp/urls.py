from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
from homeapp import views
from assessment import views as ass_view

urlpatterns = [
    
    path('about/', views.about, name="about"),
    
    path('', views.index),
    
    
    #path('assessment/', include('assessment.urls'), namespace="assessment")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)