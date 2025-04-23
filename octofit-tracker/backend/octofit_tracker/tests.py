from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="pass1234")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email="teamuser@example.com", name="Team User", password="pass1234")
        team = Team.objects.create(name="Team A")
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="activity@example.com", name="Activity User", password="pass1234")
        activity = Activity.objects.create(user=user, activity_type="run", duration=30)
        self.assertEqual(activity.activity_type, "run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="workout@example.com", name="Workout User", password="pass1234")
        workout = Workout.objects.create(user=user, workout_type="strength", details={"sets": 3})
        self.assertEqual(workout.workout_type, "strength")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Leaderboard Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100, week="2025-W17")
        self.assertEqual(leaderboard.points, 100)
