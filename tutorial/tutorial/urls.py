from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^user/register/', views.AddUser.as_view()),
#    url(r'^register/',views.register, name='register'),
#    url(r'^success/',views.success, name='success'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
