from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response(token.key)
class UserList(APIView):
    def get(self,request):
        model=Users.objects.all()
        serializer=UserSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserDetail(APIView):
    def get_user(self,employee_id):
        try:
            model=Users.objects.get(id=employee_id)
            return model

        except Users.DoesNotExist:
            return None


    def get(self,request,employee_id):
        if not self.get_user(employee_id):
            return Response(f"(User with {employee_id} does not exist)",status=status.HTTP_404_NOT_FOUND)

        
 

        serializer=UserSerializer(self.get_user(employee_id))
        return Response(serializer.data)

    def put(self,request,employee_id):
        if not self.get_user(employee_id):
            return Response(f"(User with {employee_id} does not exist)",status=status.HTTP_404_NOT_FOUND)
  
        serializer=UserSerializer(self.get_user(employee_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,employee_id):
        if not self.get_user(employee_id):
            return Response(f"(User with {employee_id} does not exist)",status=status.HTTP_404_NOT_FOUND)

        model=self.get_user(employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
