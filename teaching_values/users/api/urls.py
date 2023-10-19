from django.urls import path
from django.conf import settings

from rest_framework.routers import DefaultRouter, SimpleRouter
from teaching_values.users.api.views import RetrieveUserView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "users"
urlpatterns = router.urls
urlpatterns += [
    path("rest-auth/user/", RetrieveUserView.as_view(), name="retrieve_user"),
]
