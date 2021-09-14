from django.urls import path
from django.views.generic import TemplateView

from articleapp import views
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ArticleListView, ArticleListView6, ArticleListView1, ArticleListView2, ArticleListView3, ArticleListView4, \
    ArticleListView5, ArticleHomeView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list_all'),

    path('language_study/', ArticleListView1.as_view(), name='list_lang'),
    path('employment/', ArticleListView2.as_view(), name='list_employ'),
    path('public_officer/', ArticleListView3.as_view(), name='list_public'),
    path('hobby/', ArticleListView4.as_view(), name='list_hobby'),
    path('programming/', ArticleListView5.as_view(), name='list_coding'),
    path('other/', ArticleListView6.as_view(), name='list_other'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),

    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

    path('search/', views.SearchFormView.as_view(), name='search'),

    path('home/', ArticleHomeView.as_view(), name='home')
]