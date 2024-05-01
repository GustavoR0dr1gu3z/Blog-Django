from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'description', 'order', 'created_at']


class PostSerializerV2(ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'description', 'created_at']