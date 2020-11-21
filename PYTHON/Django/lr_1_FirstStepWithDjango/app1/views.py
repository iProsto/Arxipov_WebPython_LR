from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

# from django.template.response import TemplateResponse
  
# def index(request):
#     return TemplateResponse(request,  "index.html")