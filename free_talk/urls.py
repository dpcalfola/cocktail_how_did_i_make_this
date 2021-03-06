from django.urls import path
from . import views

app_name = 'free_talk'

urlpatterns = [
    # path('', views.PostListView.as_view(), name='board'),
    path('', views.board, name='board'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('deleted/', views.deleted, name='deleted'),
]
