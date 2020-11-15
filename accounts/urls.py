from django.urls import path
from .views import UserList, UserUpdate

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserUpdate.as_view()),
]