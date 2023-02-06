from django.contrib import admin
from django.urls import include, path
from projectfiles.library import doNothing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('doNothing', doNothing, name='doNothing'),
]