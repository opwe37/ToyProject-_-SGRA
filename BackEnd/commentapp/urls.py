from django.urls import path

from commentapp.views import CommentCreateView, CommentListView, CommentDeleteView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('list/', CommentListView.as_view(), name='list'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]