from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Question, Answer, Quiz


""" Testing the models """

class CustomUserModelTest(TestCase):

    def test_string_representation(self):
        user = CustomUser(firstname="John", lastname="Doe", email="john.doe@example.com")
        self.assertEqual(str(user), user.firstname + " " + user.lastname)

    def test_user_creation(self):
        user = CustomUser.objects.create(firstname="John", lastname="Doe", email="john.doe@example.com")
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.__str__(), user.firstname + " " + user.lastname)

class QuestionModelTest(TestCase):

    def test_string_representation(self):
        question = Question(text="What's 2 + 2?", option1="1", option2="2", option3="3", option4="4", correct_option=2)
        self.assertEqual(str(question), question.text)

    def test_question_creation(self):
        question = Question.objects.create(text="What's 2 + 2?", option1="1", option2="2", option3="3", option4="4", correct_option=2)
        self.assertTrue(isinstance(question, Question))
        self.assertEqual(question.__str__(), question.text)

class AnswerModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(firstname="John", lastname="Doe", email="john.doe@example.com")
        self.question = Question.objects.create(text="What's 2 + 2?", option1="1", option2="2", option3="3", option4="4", correct_option=2)

    def test_answer_creation(self):
        answer = Answer.objects.create(user=self.user, question=self.question, selected_option=2)
        self.assertTrue(isinstance(answer, Answer))
        self.assertEqual(answer.selected_option, 2)

class QuizModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(firstname="John", lastname="Doe", email="john.doe@example.com")

    def test_quiz_creation(self):
        quiz = Quiz.objects.create(user=self.user)
        self.assertTrue(isinstance(quiz, Quiz))

""" register view test should test if the registration view:
1. Renders the correct template.
2. Properly saves a user when valid data is submitted.
3. Redirects to the quiz start page upon successful registration."""

class RegisterViewTest(TestCase):

    def test_register_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(reverse('register'), data={'firstname': 'John', 'lastname': 'Doe', 'email': 'john.doe@example.com'})
        
        self.assertEqual(CustomUser.objects.count(), 1)
        new_user = CustomUser.objects.first()
        self.assertEqual(new_user.firstname, 'John')

    def test_redirects_after_POST(self):
        response = self.client.post(reverse('register'), data={'firstname': 'John', 'lastname': 'Doe', 'email': 'john.doe@example.com'})
        new_user = CustomUser.objects.first()
        self.assertRedirects(response, reverse('quiz_start', args=(new_user.id,)))


""" To test if the quiz start view renders the right template """
class QuizStartViewTest(TestCase):

    def test_quiz_start_view_uses_correct_template(self):
        user = CustomUser.objects.create(firstname="John", lastname="Doe", email="john.doe@example.com")
        response = self.client.get(reverse('quiz_start', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz_start.html')


  
