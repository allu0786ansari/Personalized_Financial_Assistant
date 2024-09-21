# finance/forms.py
from django import forms
from .models import Transaction

class TransactionFilterForm(forms.Form):
    transaction_type = forms.ChoiceField(
        choices=[('', 'All'), ('income', 'Income'), ('expense', 'Expense')],
        required=False
    )
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.CharField(required=False, max_length=255)
