#Quiz API
A Django REST Framework (DRF) backend for managing quizzes, supporting time-limited attempts, multiple-choice questions, student answers, and educator quiz creation.


#Features
✅ Quiz Management
Educators can create quizzes with multiple questions and answers.
Each quiz can have an optional time limit (duration_minutes).

✅ Question & Answer Management
Supports multiple-choice questions.
Each answer has a boolean is_correct flag.
Students can submit answers per question.

✅ Time-Limited Quizzes
Each quiz can have a duration_minutes limit.
Tracks when the attempt starts (started_at) and finishes (completed_at).
Prevents submission if time expires.

✅ Student Quiz Attempts
Tracks quiz attempts per student.
Calculates and stores score automatically.
Optionally prevents multiple attempts per quiz.

✅ APIs
List all quizzes
Retrieve a single quiz
Create a quiz (educators only)
Submit/attempt a quiz
View quiz attempt history