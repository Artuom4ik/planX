from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializator import UserSerializer


class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({'error': 'Некорректные данные. Проверьте логин и пароль'},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def get_password(request):
        try:
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')
            return {"old_password": old_password, "new_password": new_password}
        except Exception:
            raise Http404

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        try:
            user = request.user
            passwords = self.get_password(request)
            old_password = passwords.get('old_password')
            new_password = passwords.get('new_password')

            if not user.check_password(old_password):
                return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password successfully changed'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
