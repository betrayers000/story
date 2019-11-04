from django.urls import path
from . import views

app_name="storys"

urlpatterns = [
    path('storys/', views.story_get),
    path('storys/<int:id>/', views.story_detail),
    path('<int:id>/images/', views.image_get),
    path('<int:id>/comment/', views.comment),
]
