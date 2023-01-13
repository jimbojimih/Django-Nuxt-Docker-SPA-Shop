from rest_framework import views, status, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


def auto_creations_of_users(request):
    if request.user.is_anonymous:
        last_id = User.objects.all().last().id
        username = f'GuestUser {int(last_id)+1}'
            
        user = User.objects.create_user(username=username)
        profile = Profile.objects.create(user=user)
        user.save() 
        profile.save()
        
        #user = authenticate(username=username, password=password)
        login(request, user) 


class UserView(views.APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def patch(self, request):
        user = self.request.user
      
        serializer = UserSerializer(user, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, 
                        data=serializer.errors)

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

