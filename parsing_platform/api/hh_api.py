import requests


class HHAPI:
    BASE_URL = 'https://api.hh.ru/'

    @staticmethod
    def get_vacancies():
        response = requests.get(f'{HHAPI.BASE_URL}vacancies')
        return response.json()

    @staticmethod
    def get_applicants():
        response = requests.get(f'{HHAPI.BASE_URL}resumes')
        return response.json()

    @staticmethod
    def search_vacancies(query):
        params = {
            'text': query,
            'per_page': 10  # ограничим количество результатов
        }
        response = requests.get(f'{HHAPI.BASE_URL}vacancies', params=params)
        if response.status_code == 200:
            return response.json()
        return None
