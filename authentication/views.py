from rest_framework import generics, status, views, permissions
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    