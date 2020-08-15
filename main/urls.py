from django.urls import path
from main import views
urlpatterns = [
    path('index',views.index),
    path('article/<int:pk>',views.article,name='get_article'),
    path('author/<int:pk>',views.author,name='get_author'),
]