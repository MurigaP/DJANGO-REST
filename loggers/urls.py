
from django.conf.urls import include,url
from django.contrib import admin
from inventory.admin import admin_site
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^abcdefgh/', include(admin.site.urls)),
    url(r'^inventory/', admin_site.urls),
    #url(r'^', include('inventory.urls')),



]
urlpatterns=format_suffix_patterns(urlpatterns)
