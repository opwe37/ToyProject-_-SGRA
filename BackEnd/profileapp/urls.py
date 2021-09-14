from django.urls import path

from profileapp.views import ProfileDetailView

app_name = "profileapp"

urlpatterns = [
    path('detail/<int:pk>', ProfileDetailView.as_view(), name="detail"),
]
