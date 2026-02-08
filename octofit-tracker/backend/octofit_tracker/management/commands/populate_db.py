from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Example models for demonstration (replace with your actual models)
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=ironman, score=100)
        app_models.Leaderboard.objects.create(user=batman, score=90)

        # Create workouts
        app_models.Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        app_models.Workout.objects.create(name='Speed Run', description='Speed workout for heroes')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
