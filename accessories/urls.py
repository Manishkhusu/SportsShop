from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('home/', home_page, name='home_page'),
    path ('signup/', user_signup , name = 'sign_up'),
    path ('home/logout/' , logout_view , name = 'logout')
]
