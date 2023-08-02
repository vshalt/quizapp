from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Country
import random


def get_question_details():
    countries = Country.objects.all()
    countries = [country for country in countries]
    country = random.choice(countries)
    options = []
    options.append(country.capital)
    random.shuffle(countries)
    for entry in countries:
        if entry.capital not in options:
            options.append(entry.capital)
        if len(options) == 4:
            break
    random.shuffle(options)
    return country.name, options

def home(request):
    if request.method == "POST":
        country_quiz = request.POST["country"]
        user_response = request.POST["answer"]
        try:
            country = Country.objects.get(name=country_quiz)
            if country.capital == user_response:
                messages.add_message(request, messages.INFO, "Correct answer", extra_tags="success")
            else:
                messages.add_message(request, messages.INFO, "Wrong answer", extra_tags="danger")
        except Country.DoesNotExist:
            pass
        country, options = get_question_details()
    else:
        country, options = get_question_details()
    return render(request, "home.html", {"question": True, "country": country, "options": options})

