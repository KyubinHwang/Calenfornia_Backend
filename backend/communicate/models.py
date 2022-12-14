from django.db import models
from django.conf import settings
from accounts.models import User
from info.models import Info
from subjects.models import Subject
# 일정에 대한 댓글 기능
class Comment(models.Model):
    commnetInfo = models.ForeignKey(Info, null=False, blank=False, on_delete=models.CASCADE) #일정에 대한 fk를 받기
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) #야자수 1, 2, 3 처럼 user_id
    created_at = models.DateField(auto_now_add=True, null=False, blank=False) # 생성일자
    comment = models.TextField()
    subject_id = models.ForeignKey(Subject,related_name = 'subject_comment',on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    # def like_count():
    #     return self.likes.count()

    # def dislike_count():
    #     return self.dislikes.count()