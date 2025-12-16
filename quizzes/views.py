from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import IsEducator

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsEducator]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
