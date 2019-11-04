from django.shortcuts import render, get_object_or_404
from .models import Story, StoryImage, Comment
from .serializers import StorySerializer, ImageSerializer, StoryDetailSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

SUCCES_MESSAGE = {'message':'success'}

@api_view(['GET', 'POST'])
def story_get(request):
    if request.method == "GET":
        storys = Story.objects.all()
        serializer = StorySerializer(storys, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user.id)
            return Response(SUCCES_MESSAGE)

@api_view(['GET', 'POST'])
def image_get(request, id):
    if request.method == "GET":
        images = StoryImage.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(story_id=id)
            return Response(SUCCES_MESSAGE)

@api_view(['GET', 'PUT', 'DELETE'])
def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    if request.method == "GET":
        serializer = StoryDetailSerializer(story)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StorySerializer(data=request.data, instance=story)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(SUCCES_MESSAGE)
    elif request.method == "DELETE":
        story.delete()
        return Response(SUCCES_MESSAGE)
    