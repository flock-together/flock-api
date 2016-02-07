from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('api.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    # Creates login button for browsable site
    url(r'^api-auth/', include('rest_framework.urls')),
]
