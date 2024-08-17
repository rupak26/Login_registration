from .models import login,registration,Todo
from .serializers import loginSerializer,registrationSerializer,TodoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from rest_framework.exceptions import NotAuthenticated
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class userRegistrationView(APIView):
    permission_classes = []
    def post(self,request):
        serializer = registrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class userLoginView(APIView):
    permission_classes = []
    def post(self,request):
        serializer = loginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = registration.objects.get(email = email)
            if user is not None:
               return Response({ "token" : get_tokens_for_user(user)})     
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)