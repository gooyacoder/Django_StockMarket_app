from django.shortcuts import render



def home(request):

	import json
	import requests

	# API KEY : e759076faa64ada2e1d120b9fdd68771
	# Company Quote : https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo


	if request.method == 'POST':
		ticker = request.POST['ticker']
		try:
			cq_request = requests.get('https://financialmodelingprep.com/api/v3/quote/' + ticker + '?apikey=e759076faa64ada2e1d120b9fdd68771')
			api = json.loads(cq_request.content)
			return render(request, "home.html", {'api': api[0]})
		except Exception as e:
			api = 'Error'
			return render(request, "home.html", {'api': api})

	else:
		return render(request, "home.html", {'ticker': 'Please enter the ticker.'})
	
	# api = json.loads(cq_request.content)

	# return render(request, "home.html", {'api': api[0]})

def about(request):
	return render(request, "about.html", {})

def add_stock(request):
	return render(request, "add_stock.html", {})