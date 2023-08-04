from django.apps import apps
from django.contrib import admin

# Get all the installed apps
app_models = apps.get_models()

# Register each model with the admin site
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
