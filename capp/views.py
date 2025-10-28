from django.shortcuts import render, redirect
import requests
# Create your views here.

def index(request):
	cname = request.GET.get("cname")
	if cname == None:
		cname = "india"
	print(cname)
	url = f'https://disease.sh/v3/covid-19/countries/{cname}'
	r = requests.get(url)
	data = r.json()
	print(data)
	return render(request, 'index.html', {'data':data})
