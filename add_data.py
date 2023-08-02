import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz.settings")
django.setup()

from quizapp.models import Country

def get_data():
    try:
        response = requests.get("https://countriesnow.space/api/v0.1/countries/capital")
        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.RequestException(
                f"Status: {response.status_code}, Response: {response.text}"
            )
    except requests.exceptions.RequestException as e:
        print(f"Error while trying to get data from external source: {e}")

def add_country(name, capital):
    if name and capital:
        country = Country.objects.create(name=name, capital=capital)
        country.save()

if __name__ == "__main__":
    try:
        response = get_data()
        if response.get("error"):
            raise Exception(response.get("msg"))
        for country in response.get("data", []):
            add_country(country.get("name"), country.get("capital"))
    except Exception as e:
        print(e)
        raise


