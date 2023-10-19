from django.urls import include, path

app_name = "api"
urlpatterns = [
    # User
    path("", include("teaching_values.users.api.urls")),
]
