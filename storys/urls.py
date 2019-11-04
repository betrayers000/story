from django.urls import path
from . import views

app_name="storys"

urlpatterns = [
    path('storys/', views.story_get),
    path('storys/<int:id>/', views.story_detail),
    path('images/<int:id>/', views.image_get),
]
