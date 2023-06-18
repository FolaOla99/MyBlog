from django.urls import path
from .views import BlogListView,BlogDetailView

urlpatterns = [
        path('', BlogListView.as_view(), name='Home'),
        path('PostView/<int:pk>/', BlogDetailView.as_view(), name='PostView'),
]


