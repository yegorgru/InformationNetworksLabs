from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from . import utils
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404


class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        val_result = utils.validate_signup_info(username, password, email)
        if val_result != "":
            return Response({'error': val_result}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            User.objects.create_user(username, email, password)
            return Response({'message': 'Signup successful.'}, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            try:
                username = User.objects.get(email=username.lower()).username
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                user = None
            if user is not None:
                login(request, user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        date_param = self.kwargs.get('date', None)
        try:
            if date_param:
                tasks = Task.objects.filter(user=request.user, date=date_param)
            else:
                raise ValueError('Date parameter is required')

            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)


class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        description = request.data.get('description')
        date = request.data.get('date')

        task = Task.objects.create(
            user=request.user,
            name=name,
            description=description,
            date=date,
            status=False
        )
        task.save()

        response_data = {
            'message': 'Task created successfully.'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        task_id = request.data.get('taskId')

        if task_id is None:
            return Response({'error': 'Task ID is required in the request data.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        task.name = request.data.get('name', task.name)
        task.description = request.data.get('description', task.description)
        task.date = request.data.get('date', task.date)

        task.save()
        response_data = {
            'message': 'Task updated successfully.'
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        task_id = request.data.get('taskId')

        if task_id is None:
            return Response({'error': 'Task ID is required in the request data.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        response_data = {
            'message': 'Task deleted successfully.'
        }

        return Response(response_data, status=status.HTTP_200_OK)


class TaskDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompleteTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task_id = request.data.get('taskId')

        if task_id is None:
            return Response({'error': 'Task ID is required in the request data.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        task.status = True
        task.save()

        response_data = {
            'message': 'Task completed successfully.'
        }

        return Response(response_data, status=status.HTTP_200_OK)
