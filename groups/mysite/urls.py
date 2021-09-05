#;mysite

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('groups/', include('groups.urls')),
    path('admin/', admin.site.urls),
]