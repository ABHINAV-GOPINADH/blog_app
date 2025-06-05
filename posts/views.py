from rest_framework import serializers, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer
from rest_framework import viewsets, permissions, filters
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend

# Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)