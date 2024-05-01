from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(ViewSet):
    def list(self, request):        
        serializerData = PostSerializer(
            Post.objects.all(), 
            many=True # Devolver array completo
        )
        return Response(            
            status  =   status.HTTP_200_OK, 
            data    =   serializerData.data
        )
    
    def retrieve(self, request, pk: int):
        post = PostSerializer(
            Post.objects.get(pk=pk)
        )
        return Response(
            status = status.HTTP_200_OK,
            data = post.data
        )
    
    def create(self, request):
        serializer = PostSerializer(
            data = request.POST
        )
        serializer.is_valid(
            raise_exception = True
        )
        serializer.save()
        
        return Response(
            status = status.HTTP_200_OK,
            data = serializer.data
        )

'''class PostAPIView(APIView):
    def get(self, request):        
        serializerData = PostSerializer(
            Post.objects.all(), 
            many=True # Devolver array completo
        )
        return Response(            
            status  =   status.HTTP_200_OK, 
            data    =   serializerData.data

        )
    
    def post(self, request):
        serializer = PostSerializer(
            data = request.POST
        )
        serializer.is_valid(
            raise_exception = True
        )
        serializer.save()
        
        return Response(
            status = status.HTTP_200_OK,
            data = serializer.data
        )'''


    


    