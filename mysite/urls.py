from django.contrib import admin
from django.urls import path, include
from backend import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls.urlpatterns)),
]
