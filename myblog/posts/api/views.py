from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post

class PostAPIView(APIView):
    def get(self, request):
        #posts = Post.objects.all()

        #Array de los titulos de post
        posts = [
            post.title for post in Post.objects.all()
        ]

        
        return Response(            
            status  =   status.HTTP_200_OK, 
            data    =   posts
        )

    