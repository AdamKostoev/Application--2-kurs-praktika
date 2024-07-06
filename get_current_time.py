import os
import django
from django.utils import timezone

# Установите переменную среды DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parsing_platform.settings')

# Инициализируйте Django
django.setup()

# Получите текущее время
current_time = timezone.now()
print(current_time)
