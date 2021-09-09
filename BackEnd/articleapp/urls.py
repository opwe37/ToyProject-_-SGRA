from django.urls import path
from django.views.generic import TemplateView

from articleapp import views
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ArticleListView, ArticleListView6, ArticleListView1, ArticleListView2, ArticleListView3, ArticleListView4, \
    ArticleListView5, ArticleHomeView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),

    path('language_study/', ArticleListView1.as_view(), name='list'),
    path('employment/', ArticleListView2.as_view(), name='list'),
    path('public_officer/', ArticleListView3.as_view(), name='list'),
    path('hobby/', ArticleListView4.as_view(), name='list'),
    path('programming/', ArticleListView5.as_view(), name='list'),
    path('other/', ArticleListView6.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),

    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

    path('search/', views.SearchFormView.as_view(), name='search'),

    path('home/', ArticleHomeView.as_view(), name='home')
]