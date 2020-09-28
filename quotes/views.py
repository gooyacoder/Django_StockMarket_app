from django.shortcuts import render


# API KEY : UWEXKNCGYISWNLMJ
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo

def home(request):

	import json
	import requests

	api_request = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=UWEXKNCGYISWNLMJ')
	api = json.loads(api_request.content)

	return render(request, "home.html", {'api': api})

def about(request):
	return render(request, "about.html", {})