from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Подключение к MongoDB
        host = settings.DATABASES['default'].get('HOST') or 'localhost'
        port = int(settings.DATABASES['default'].get('PORT') or 27017)
        client = MongoClient(host, port)
        db = client[settings.DATABASES['default']['NAME']]

        # Очистка коллекций
        db.user.drop()
        db.team.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Создание пользователей
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thunder God', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Metal Geek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Zero Cool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Crash Override', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Создание команд
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        blue_team.save()
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        gold_team.save()
        blue_team.members.add(users[0])
        blue_team.members.add(users[1])
        blue_team.members.add(users[2])
        gold_team.members.add(users[3])
        gold_team.members.add(users[4])

        # Создание активностей
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Велоспорт', duration=60, distance=20.0, timestamp=datetime.now()),
            Activity(_id=ObjectId(), user=users[1], activity_type='Кроссфит', duration=120, distance=None, timestamp=datetime.now()),
            Activity(_id=ObjectId(), user=users[2], activity_type='Бег', duration=90, distance=15.0, timestamp=datetime.now()),
            Activity(_id=ObjectId(), user=users[3], activity_type='Силовая', duration=30, distance=None, timestamp=datetime.now()),
            Activity(_id=ObjectId(), user=users[4], activity_type='Плавание', duration=75, distance=2.5, timestamp=datetime.now()),
        ]
        Activity.objects.bulk_create(activities)

        # Создание таблицы лидеров
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=blue_team, points=250, week='2025-W17'),
            Leaderboard(_id=ObjectId(), team=gold_team, points=180, week='2025-W17'),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Создание тренировок
        workouts = [
            Workout(_id=ObjectId(), user=users[0], workout_type='Велотренировка', details={'desc': 'Тренировка к велозаезду'}, timestamp=datetime.now()),
            Workout(_id=ObjectId(), user=users[1], workout_type='Кроссфит', details={'desc': 'Кроссфит-сессия'}, timestamp=datetime.now()),
            Workout(_id=ObjectId(), user=users[2], workout_type='Бег', details={'desc': 'Подготовка к марафону'}, timestamp=datetime.now()),
            Workout(_id=ObjectId(), user=users[3], workout_type='Силовая', details={'desc': 'Силовые упражнения'}, timestamp=datetime.now()),
            Workout(_id=ObjectId(), user=users[4], workout_type='Плавание', details={'desc': 'Тренировка по плаванию'}, timestamp=datetime.now()),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('База данных octofit_db успешно заполнена тестовыми данными.'))
