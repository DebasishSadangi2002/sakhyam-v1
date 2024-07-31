# urls.py
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import member_create, member_list

urlpatterns = [
    
    path('members/add/', member_create, name='member_create'),
    path('members/', member_list, name='member_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
