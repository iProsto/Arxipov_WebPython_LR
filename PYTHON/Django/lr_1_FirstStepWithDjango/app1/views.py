from django.shortcuts import render

def index(request):
	return render(request, 'summary/index.html')

def summary_w(request):
	return render(request, 'summary/summary_w.html')

def index_no_creative(request):
	return render(request, 'summary/index_no_creative.html')

def summary_w_no_creative(request):
	return render(request, 'summary/summary_w_no_creative.html')

# from django.template.response import TemplateResponse
  
# def index(request):
#     return TemplateResponse(request,  "index.html")