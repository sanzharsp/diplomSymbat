from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serilaizers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Create your views here.



class AuthorizateView(TokenObtainPairView):
    serializer_class = AuthorizateSerializer
    


class RegistrationView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    def post(self, request):
        

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(username=serializer.data['username'],email=serializer.data['email'])
        if user.exists():
            return Response({"error":"Пользователь уже существует в системе"},status=status.HTTP_400_BAD_REQUEST)

        else:
            new_user = User.objects.create_user(
                        username = request.data["username"],
                        first_name = request.data["first_name"],
                        last_name = request.data["last_name"],
                        password = request.data["password"],
                        surname = request.data["surname"],
                        email = request.data["email"],
                        )
            new_profile = Profile.objects.create(
                        user = new_user,
                        nameResidentialComplex = request.data["nameResidentialComplex"],
                        entrance = request.data["entrance"],
                        floor = request.data["floor"],
                        roomNumber = request.data["roomNumber"],
                        )
            refresh = RefreshToken.for_user(new_user)
            return Response({'user':serializer.data, 
                    'profile_user':ProfileSerilizer(new_profile).data,  
                    'is_superuser':new_user.is_superuser,   
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    }, status=status.HTTP_201_CREATED)
