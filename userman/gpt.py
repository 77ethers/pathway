import os
import openai
import json
from prompt import prompts
openai.api_key = "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"

def curriculum_generator():
    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": prompts["curriculum_steps"]},
        {"role": "user", "content": json.dumps({
            "id": 1,
            "name": "Ankita",
            "whatsapp_number": "8979564668",
            "learning_goal": "Personal Development (e.g., Leadership 👑, Communication 💬, Time Management ⏳)",
            "target_date": "2024-07-24(1 year)",
            "current_skill_level": 4,
            "sub_skills": "Work life balance",
            "daily_time_dedication": "1Hour",
            "preferred_learning_time": "Night",
            "learning_preference": "Books",
            "progress_tracking_preference": 'true',
        })}
    ]
    )
    print(completion.choices[0].message["content"])
    return completion.choices[0].message["content"]

def pathway_builder():
    completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": "You are an expert learning pathway creator from 'Team Pathway'. You build learning pathway document for our customers based on the analysed curriculum requirements. This document is for them to keep, revisit and stay motivated."},
        {"role":"user", "content": prompts["document_create"]},
        {"role": "user", "content": "Creating a customized curriculum for Ankita focusing on her goal of personal development with an emphasis on work-life balance:\\n\\n1. **Identify Key Topics**: Ankita's sub-skill focus is work-life balance. Key topics related to this are:\\n   - Understanding Work-Life Balance\\n   - Role of Time Management\\n   - Stress Management\\n   - Mindfulness and Emotional Intelligence\\n   - Delegation and Prioritization\\n   - Building Healthy Habits\\n\\n2. **Structure the Learning Path**: We'll structure the learning sequence in a way that builds upon each subsequent topic:\\n   - Understanding Work-Life Balance\\n   - Role of Time Management\\n   - Delegation and Prioritization\\n   - Stress Management \\n   - Mindfulness and Emotional Intelligence\\n   - Building Healthy Habits\\n\\n3. **Choose Learning Material**: For each topic, find books apt for her current skill level:\\n   - Book1: 'Work Simply' by Carson Tate (Understanding Work-Life Balance)\\n   - Book2: 'Eat that frog!' by Brian Tracy (Role of Time Management)\\n   - Book3: 'Essentialism: The Disciplined Pursuit of Less' by Greg McKeown (Delegation and Prioritization)\\n   - Book4: '10% Happier' by Dan Harris (Stress Management)\\n   - Book5: 'Emotional Intelligence 2.0' by Travis Bradberry (Mindfulness and Emotional Intelligence)\\n   - Book6: 'Atomic Habits' by James Clear (Building Healthy Habits)\\n        \\n4. **Breakdown into Daily Tasks**: Reading for 1 hour, roughly 20-30 pages daily, would be manageable for Ankita.\\n\\n5. **Set Milestones**: Completing each book can be a milestone for Ankita. That would give her six milestones to complete.\\n\\n6. **Create a Timeline**: If she dedicates 1 hour daily, she can complete each book in about one month. Therefore, the entire timeline can be structured over six months. Get started immediately: finish the first book by August 24th, the second by September 24th, and keep moving forward with a book every month.\\n\\n7. **Add Assessments/Feedback**: Make use of reflection questions at the end of each chapter, quizzes or journals where she can note down her insights and improvements.\\n\\n8. **Provide Supportive Content**: Provide daily motivational quotes or success stories of people who've improved their work-life balance.\\n\\n9. **Review and Iterate**: Ask Ankita for her feedback and make adjustments to the curriculum as necessary.\\n\\n10. **Progress Tracking**: Implement a progress tracking system to visualize Ankita's successful completion of the milestones. This will keep her motivated to continue her learning."
        }
    ]
    )
    print(completion.choices[0].message["content"])

pathway_builder()