from django.shortcuts import render

def index(request):
	return render(request, 'summary/index.html')

def summary_w(request):
	return render(request, 'summary/summary_w.html')

# from django.template.response import TemplateResponse
  
# def index(request):
#     return TemplateResponse(request,  "index.html")