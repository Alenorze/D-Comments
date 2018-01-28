from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from sku import views


#Swagger Docs
schema_view = get_swagger_view(title='Pastebin API')

# Routers provide a way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^swagger/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
