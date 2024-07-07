from datetime import datetime
from decimal import Decimal
import requests
from django.shortcuts import render
from .models import Vacancy


def save_vacancies_to_db(vacancies):
    try:
        for vacancy_data in vacancies:
            if vacancy_data:
                # Проверяем и задаем значения по умолчанию
                salary_data = vacancy_data.get('salary') or {}
                employer_data = vacancy_data.get('employer') or {}
                snippet_data = vacancy_data.get('snippet') or {}
                type_data = vacancy_data.get('type') or {}

                # Публикуемая дата может отсутствовать или быть некорректной
                published_at = vacancy_data.get('published_at')
                if published_at:
                    published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z')
                else:
                    published_at = datetime.now()

                Vacancy.objects.create(
                    id=vacancy_data.get('id', 'Без id'),
                    title=vacancy_data.get('name', 'Без названия'),
                    city=vacancy_data.get('area', {}).get('name', 'Не указан'),
                    salary_from=Decimal(salary_data.get('from')) if salary_data.get('from') else None,
                    salary_to=Decimal(salary_data.get('to')) if salary_data.get('to') else None,
                    currency=salary_data.get('currency', 'Не указано'),
                    description=snippet_data.get('requirement', 'Описание отсутствует'),
                    requirements=snippet_data.get('requirement', 'Требования отсутствуют'),
                    responsibilities=snippet_data.get('responsibility', 'Обязанности отсутствуют'),
                    employer_name=employer_data.get('name', 'Не указан'),
                    published_at=published_at,
                    experience=vacancy_data.get('experience', {}).get('name', 'Не указан'),
                    employment=type_data.get('name', 'Не указано'),
                    remote_work=type_data.get('id') == 'remote'
                )
    except Exception as e:
        print(f"Error saving vacancies: {e}")


def clear_database():
    Vacancy.objects.all().delete()


def get_vacancies_from_api(search_query, city, min_salary, max_salary):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': search_query,
        'area': '1',  # ID региона, например, '1' для Москвы
        'page': 0,
        'per_page': 20,
        'salary_from': min_salary,
        'salary_to': max_salary,
        'city': city
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")
        return []


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'all_vacancies.html', {'vacancies': vacancies})


def index(request):
    if request.method == 'POST':
        clear_database()
        search_query = request.POST.get('search_query')
        city = request.POST.get('city')
        min_salary = request.POST.get('min_salary')
        max_salary = request.POST.get('max_salary')
        vacancies = get_vacancies_from_api(search_query, city, min_salary, max_salary)
        save_vacancies_to_db(vacancies)
        return render(request, 'index.html', {'vacancies': vacancies})
    else:
        vacancies = Vacancy.objects.all()
        return render(request, 'index.html', {'vacancies': vacancies})
