from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('quiz_start/<int:user_id>/', views.quiz_start, name='quiz_start'),
    path('quiz_question/<int:user_id>/<int:question_id>/', views.quiz_question, name='quiz_question'),
]
