from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
        path('', BlogListView.as_view(), name='Home'),
        path('PostView/<int:pk>/', BlogDetailView.as_view(), name='PostView'),
        path("post/new/", BlogCreateView.as_view(), name="post_new"),
        path("PostEdit/<int:pk>/", BlogUpdateView.as_view(), name="PostEdit"),
        path("PostDelete/<int:pk>/delete/", BlogDeleteView.as_view(), name="PostDelete")
]


