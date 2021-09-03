from django.urls import path

from freearticleapp import views
from freearticleapp.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView

app_name = 'freearticleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),

    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

    path('search/', views.SearchFormView.as_view(), name='search'),
]
