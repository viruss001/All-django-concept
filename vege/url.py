from django.urls import path
from vege import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.vege),
    path('/dele-rec/<id>/',views.dele,name="dele"),
    path('/upd-rec/<id>/',views.upda,name="dele"),
    path('/api-home/',views.api_home)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()