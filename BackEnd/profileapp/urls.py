from django.urls import path

from profileapp.views import ProfileDetailView, ProfileUpdateRView

app_name = "profileapp"

urlpatterns = [
    path('detail/<int:pk>', ProfileDetailView.as_view(), name="detail"),
    path('update/<int:pk>', ProfileUpdateRView.as_view(), name="update"),
]
