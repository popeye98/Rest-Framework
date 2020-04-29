from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

# Create your views here.
# def test_view(request):
#     data={
#         'name':'John',
#         'age':23


#     }
#     return JsonResponse(data)

from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post


class TestView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,request,*args,**kwargs):
        qs=Post.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(serializer.data)    
        

    def post(self,request,*args,**kwargs):
        serializers=PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)



class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()