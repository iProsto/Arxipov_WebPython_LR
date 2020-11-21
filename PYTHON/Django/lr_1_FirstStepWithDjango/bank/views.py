from django.shortcuts import render
from django.http import HttpResponse
from .forms import User

def index(request):
	if request.method == "POST":
		name = request.POST.get("bank_login")
		return HttpResponse("<h2>Hello, {0}</h2>".format(name))
	else:
		userform = User()
		return render(request, 'bank_index.html', {'form': userform})
