from django.contrib import admin
from django.urls import (path, include)
from rest_framework_swagger.views import get_swagger_view

from . import api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', get_swagger_view(title='Docs'), name='docs'),
    path('api/', include(api_urls), name='api'),
]
