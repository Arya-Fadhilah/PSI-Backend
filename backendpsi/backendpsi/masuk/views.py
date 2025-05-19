from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Use Django's authentication system to verify credentials
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in using the Django's built-in login function
            auth_login(request, user)  # Use `auth_login` here to avoid conflict with your view function
            return redirect('pasien')  # Redirect to the pasien page or dashboard after login
        else:
            # Invalid login attempt
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'masuk/login.html')
