from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from sku import views


# Routers provide a way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
