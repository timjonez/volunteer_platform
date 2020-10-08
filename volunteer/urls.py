from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('church/', include('church.urls', namespace='church')),
    path('jobs/', include('Job.urls', namespace='job')),
    path('search/', include('search.urls', namespace='search'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)