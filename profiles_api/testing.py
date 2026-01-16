from django.contrib.auth import get_user_model
User = get_user_model()

superusers = User.objects.filter(is_superuser=True)
for u in superusers:
    print(u.username, u.email)
