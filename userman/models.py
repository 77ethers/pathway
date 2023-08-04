from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)
    learning_goal = models.CharField(max_length=100)
    target_date = models.DateField()
    current_skill_level = models.IntegerField()
    sub_skills = models.TextField()  # store as comma-separated values or JSON
    daily_time_dedication = models.CharField(max_length=10)
    preferred_learning_time = models.CharField(max_length=10)
    learning_preference = models.CharField(max_length=50)
    progress_tracking_preference = models.BooleanField(default=False)
    chat_state = models.CharField(max_length=50, default='awaiting_name')
    last_interaction_timestamp = models.DateTimeField(default=timezone.now)


class Curriculum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curriculum_text = models.TextField()

class LearningPathway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pathway_text = models.TextField()
    generation_timestamp = models.DateTimeField(auto_now_add=True)


class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interaction_text = models.TextField()
    interaction_timestamp = models.DateTimeField(auto_now_add=True)


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_completed = models.TextField()
    completion_date = models.DateTimeField(auto_now_add=True)

class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_text = models.TextField()
    due_date = models.DateField()
    completion_status = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_slug = models.CharField(max_length=30, blank=True)
    notification_text = models.TextField()
    sent_timestamp = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    feedback = models.TextField(null=True, blank=True)  # nullable, can be filled later
    feedback_timestamp = models.DateTimeField(null=True, blank=True)  # nullable

