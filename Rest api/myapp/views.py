from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .sializers import UserSerializer

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)