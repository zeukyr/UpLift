from django.urls import path
from . import views
from .views import ucalgaryView, ucalgaryDetailView, createPostView, createCommentView


urlpatterns = [
    path('Ucalgary', ucalgaryView.as_view(), name='Ucalgary'),
    path('post/<int:pk>', ucalgaryDetailView.as_view(), name='Ucalgary-detail'),
    path('create-post', createPostView.as_view(), name='create-post'),
    path('<int:pk>/create-comment', createCommentView.as_view(), name='Create-comment'),
]