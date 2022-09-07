from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'commnetInfo', 'user_id', 'created_at', 'comment',"subject_id"]

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "commnetInfo", "comment", "user_id","subject_id")

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'commnetInfo', 'user_id', 'created_at', 'comment',"subject_id"]
