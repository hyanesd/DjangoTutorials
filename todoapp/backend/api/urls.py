from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('todos/', views.ToDoListCreate.as_view(), name='list'),
    path('todos/<int:pk>/', views.ToDoRetrieveUpdateDestroy.as_view(), name='detail'),
    path('', views.apiOverview, name="api-overview"),
    path('complete/<str:pk>/', views.completeTask, name="complete-task"),
    path('signup/', signup),
    path('signup/', views.signup),
    path('login/', views.login),
]