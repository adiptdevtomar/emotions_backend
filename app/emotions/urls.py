from django.urls import path, include
from emotions import views

urlpatterns = [
    path("getEmotion/", views.getEmotionsView),
]