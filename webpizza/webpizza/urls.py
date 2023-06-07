from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('applipizza.urls')),
    path('',include('connexion.urls')),
    path('admin/', admin.site.urls),

]
