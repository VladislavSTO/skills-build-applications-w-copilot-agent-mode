from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, routers
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = "https://fluffy-space-meme-v5j4g4x4g9rfwvgj-8000.app.github.dev"
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activity': f'{base_url}/api/activity/',
        'workouts': f'{base_url}/api/workouts/',
        'leaderboard': f'{base_url}/api/leaderboard/',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
