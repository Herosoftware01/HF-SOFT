
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('roll/', include('roll.urls')),
    path('attendance/', include('attendance.urls')),
    path('lay_spreading/', include('lay_spreading.urls')),
    path('', include('welcome.urls')),
    path('', include('pwa.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STAFF_IMAGES_URL, document_root=settings.STAFF_IMAGES_ROOT)
    urlpatterns += static(settings.ORDER_IMAGES_URL, document_root=settings.ORDER_IMAGES_ROOT)
    urlpatterns += static(settings.PRO_URL, document_root=settings.PRO_ROOT)
    urlpatterns += static(settings.ALL_URL, document_root=settings.ALL_ROOT)