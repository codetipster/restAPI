from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('user-list/', views.userList, name="user-list"),
    path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
    path('register/', RegisterView.as_view(), name="Register"),
]