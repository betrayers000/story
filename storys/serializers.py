from rest_framework import serializers
from .models import Story, StoryImage, Comment

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryImage
        fields = ('image',)

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('title', 'content', 'user_id',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'user')

class StoryDetailSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source="like_users.count")
    images = ImageSerializer(source="storyimage_set", many=True)
    comments = CommentSerializer(source="comment_set", many=True)
    class Meta:
        model = Story
        fields = ('title', 'content', 'created_at', 'user', 'like_count', 'images', 'comments')