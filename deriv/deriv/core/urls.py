from django.urls import path
from . import views

urlpatterns= [
	path('', views.login, name='login'),
    path('login_with_google_account', views.login2, name='login2')

]
