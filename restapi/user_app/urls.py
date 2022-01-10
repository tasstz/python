from django.urls import path

from user_app.views import UserByToken


urlpatterns = [
    path('user/by/token/', UserByToken.as_view()),

]