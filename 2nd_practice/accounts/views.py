from django.conf import settings
from django.contrib.auth.forms import UserCreationForm # NOTE: Built-in forms
from django.shortcuts import redirect, render

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
