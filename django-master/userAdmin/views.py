from django.shortcuts import render, redirect
from demo import views,urls
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from demo import views
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('/table')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})
