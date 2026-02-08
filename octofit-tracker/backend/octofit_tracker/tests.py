from django.test import TestCase
from .models import Team, User, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10)
        self.assertEqual(str(activity), 'testuser - run')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        lb = Leaderboard.objects.create(user=user, score=50)
        self.assertEqual(str(lb), 'testuser: 50')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
