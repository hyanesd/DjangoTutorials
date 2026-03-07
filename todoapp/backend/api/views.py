from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ToDoSerializer
from todo.models import ToDo

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token


class ToDoListCreate(generics.ListCreateAPIView):

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ToDo.objects.filter(user=user).order_by('-created')
        return ToDo.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todos/',
        'Create': '/todos/',
        'Retrieve': '/todos/<id>/',
        'Update': '/todos/<id>/',
        'Delete': '/todos/<id>/',
    }
    return Response(api_urls)


@api_view(['POST'])
def completeTask(request, pk):
    task = ToDo.objects.get(id=pk)
    task.completed = True
    task.save()

    return Response('Task marked as complete')


@api_view(['POST'])
def signup(request):
    username = request.data['username']
    password = request.data['password']
    password2 = request.data['password2']

    if password == password2:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response('User created successfully')
    else:
        return Response('Passwords do not match')


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response('Invalid credentials')