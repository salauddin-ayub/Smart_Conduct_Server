from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from room import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
