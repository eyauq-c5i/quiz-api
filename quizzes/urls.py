from django.urls import path
from .views import (
    QuizCreateView,
    QuizListView,
    QuizDetailView,
    SubmitQuizView,
)

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz-create'),
    path(
        'quizzes/<int:quiz_id>/submit/',
        SubmitQuizView.as_view(),
        name='submit-quiz'
    )
]
