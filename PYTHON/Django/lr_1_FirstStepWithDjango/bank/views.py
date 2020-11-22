from django.shortcuts import render
from django.http import HttpResponse
from .forms import User



def index(request):
	user = User()
	if request.method == "POST":
		login = request.POST.get("login")
		password = request.POST.get("password")
		if password == "1111":
			return render(request, 'bank_menu.html',  context={"bank_login":login})
		else:
			return render(request, 'bank_wrong_password.html',  {'form':user})
	else:
		return render(request, 'bank_index.html', {'form':user})
