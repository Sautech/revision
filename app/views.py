from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import pyrebase


config = {
    "apiKey": "AIzaSyBtQ3RAYAwHmXlLf5SUkXUOPfKUt-0jgOs",
    "authDomain": "iothome-6bab7.firebaseapp.com",
    "databaseURL": "https://iothome-6bab7.firebaseio.com",
    "projectId": "iothome-6bab7",
    "storageBucket": "iothome-6bab7.appspot.com",
    "messagingSenderId": "191054227706",
}


firebase= pyrebase.initialize_app(config)

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    print(firebase.api_key)
    return render(request,'home.html',{})

