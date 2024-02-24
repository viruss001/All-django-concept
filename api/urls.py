from django.urls import path,include
from api import views
#from api.views import APIS
from api.views import UsernameViewSet
from api.views import Registeruser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'username', UsernameViewSet, basename='username')
urlpatterns = router.urls
urlpatterns = [
    path("/data",include(router.urls)),
    path("/regi",Registeruser.as_view()),
    path('',views.home),
    path('/geting',views.geting),
    path('/posting',views.posting),
    path('/puting/<id>/',views.puting),
    path('/patching/<id>/',views.patching),
    path('/delete/<id>/',views.delete),
    #path("/api",APIS.as_view())

    
]