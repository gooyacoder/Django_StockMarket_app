from .models import Stock
from django import forms

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['ticker']