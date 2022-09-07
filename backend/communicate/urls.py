from django.urls import path, include

from .views import CommentsAPIView, CommentAPIView, UserCommentView

urlpatterns = [
    path('comment/',CommentsAPIView.as_view()),
   # path('comment/<int:fk>/',UserCommentView.as_view()),
    path('info/<int:fk>/comment/<int:pk>/',CommentAPIView.as_view()),
] 
 