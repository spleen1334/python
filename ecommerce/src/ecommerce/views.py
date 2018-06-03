from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from accounts.forms import LoginForm, RegisterForm
from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Django!",
        "content": " Welcome to the homepage.",
    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHH"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": " Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "title": "About Page",
        "content": "Here is about page.",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.clean_data['username']
        password = form.clean_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()  # clear form data
        else:
            print("Error")

    return render(request, "contact/view.html", context)
