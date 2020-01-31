from django.urls import path, include
from user.views import CreateUserView, login, UserDetailView


urlpatterns = [
    path(
        'register/', 
   CreateUserView.as_view(), 
    ),
    path(
        'login/', login
        ),
    path(
        '<int:pk>/', UserDetailView.as_view(),
    )
]