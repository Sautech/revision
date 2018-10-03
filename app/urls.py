from django.urls import path

from app import views
from app.views import SignUp

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', SignUp.as_view(), name="signup"),
]
