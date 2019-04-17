from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('app.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^mdeditor/',include('mdeditor.urls')),
]
