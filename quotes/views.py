from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm



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
	import json
	import requests
	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, 'Stock has been added successfully.')
			return redirect('add_stock')
	else:
		tickers = Stock.objects.all()
		output = []
		for ticker in tickers:
			try:
				cq_request = requests.get('https://financialmodelingprep.com/api/v3/quote/' + str(ticker) + '?apikey=e759076faa64ada2e1d120b9fdd68771')
				api = json.loads(cq_request.content)
				api[0]['ticker'] = ticker
				api[0]['id'] = ticker.id
				output.append(api[0])
			except Exception as e:
				api = 'Error'

		return render(request, "add_stock.html", {'tickers' : tickers, 'output' : output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, 'Stock has been deleted successfully.')
	return redirect(add_stock)