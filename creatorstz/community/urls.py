from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='community-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='community-about'),
    path('entourage/', views.entourage, name='community-entourage'),
    path('dwg/', views.dwg, name='community-dwg'),
    path('icons/', views.icons, name='community-icons'),
    path('maps/', views.maps, name='community-maps'),
    path('models/', views.models, name='community-models'),
    path('scripts/', views.scripts, name='community-scripts'),
    path('tutorials/', views.tutorials, name='community-tutorials'),
]
