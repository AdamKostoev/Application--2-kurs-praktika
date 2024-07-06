import os
import sys
import django
from django.utils import timezone

# Установите переменную среды DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parsing_platform.settings')

# Добавьте путь к проекту в sys.path
sys.path.append('C:/Users/pc/Application 2 kurs praktika')
sys.path.append('C:/Users/pc/Application 2 kurs praktika/parsing_platform')

# Инициализируйте Django
django.setup()

# Получите текущее время
current_time = timezone.now()
print(current_time)
