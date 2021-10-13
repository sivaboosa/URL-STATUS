
from django.contrib import admin
from django.urls import path, include
from url.views import startTesting

urlpatterns = [
    path('url/', include('url.urls')),
    path('startTesting/', startTesting),
    path('admin/', admin.site.urls),
]
