from rest_framework import generics
from .models import User, Curriculum, LearningPathway, Notification, DailyGoal
from .serializers import UserSerializer
from .gpt import curriculum_generator, pathway_builder, generate_introductory_message, daily_plan_builder
import json
from datetime import datetime

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # save the User instance
        user = serializer.save()
        
        intro_message = generate_introductory_message(serializer.data)
        
        intro_notification = Notification(user=user, notification_slug="intro_message", notification_text=intro_message)
        intro_notification.save()


        print("generating curriculum")
        curriculum_text = curriculum_generator(serializer.data)
        curriculum = Curriculum(user=user, curriculum_text=curriculum_text)
        curriculum.save()

        print("generating pathway")
        pathway_text = pathway_builder(curriculum_text)
        pathway = LearningPathway(user=user, pathway_text=pathway_text)
        pathway.save()

        print("generating daily goals")

        daily_plan = daily_plan_builder(pathway_text, user_data=serializer.data)
        daily_goal = DailyGoal(user=user, date=datetime.now(), goal_text = daily_plan)
        daily_goal.save()

        

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
