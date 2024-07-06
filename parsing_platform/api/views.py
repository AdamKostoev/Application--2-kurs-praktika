from datetime import datetime
from decimal import Decimal
import requests
from django.shortcuts import render
from .models import Vacancy

def save_vacancies_to_db(vacancies):
    try:
        for vacancy_data in vacancies:
            if vacancy_data:
                salary_data = vacancy_data.get('salary', {})
                employer_data = vacancy_data.get('employer', {})
                snippet_data = vacancy_data.get('snippet', {})

                published_at = datetime.strptime(vacancy_data.get('published_at'), '%Y-%m-%dT%H:%M:%S%z')

                Vacancy.objects.create(
                    id=vacancy_data.get('id'),
                    title=vacancy_data.get('name', 'Без названия'),
                    city=vacancy_data.get('area', {}).get('name', 'Не указан'),
                    salary_from=Decimal(salary_data.get('from')) if salary_data.get('from') else None,
                    salary_to=Decimal(salary_data.get('to')) if salary_data.get('to') else None,
                    currency=salary_data.get('currency', 'Не указано'),
                    description=snippet_data.get('requirement', 'Описание отсутствует'),
                    requirements=snippet_data.get('requirement', 'Требования отсутствуют'),
                    responsibilities=snippet_data.get('responsibility', 'Обязанности отсутствуют'),
                    employer_name=employer_data.get('name', 'Не указан'),
                    published_at=published_at
                )
    except Exception as e:
        print(f"Error saving vacancies: {e}")

def clear_database():
    Vacancy.objects.all().delete()

def get_vacancies_from_api(search_query):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': search_query,
        'area': '1',  # ID региона, например, '1' для Москвы
        'page': 0,
        'per_page': 10
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")
        return []

def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'index.html', {'vacancies': vacancies})

def search_vacancy(request):
    if request.method == 'POST':
        clear_database()
        search_query = request.POST.get('search_query')
        vacancies = get_vacancies_from_api(search_query)
        save_vacancies_to_db(vacancies)
        return render(request, 'index.html', {'vacancies': vacancies})
    elif request.method == 'GET' and 'id' in request.GET:
        try:
            vacancy_id = request.GET.get('id')
            if vacancy_id.isdigit():
                vacancies = Vacancy.objects.filter(id=int(vacancy_id))
                return render(request, 'index.html', {'vacancies': vacancies})
            else:
                return render(request, 'index.html', {'vacancies': Vacancy.objects.all()})
        except ValueError:
            return render(request, 'index.html', {'vacancies': Vacancy.objects.all()})
    return render(request, 'search_vacancy.html')