from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from stent import views

router = routers.DefaultRouter()
router.register(r'airways', views.AirwayViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
