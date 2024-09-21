from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionFilterForm
from django.db.models import Sum


@login_required
def advice(request):
    return render(request, "finance/advice.html")

@login_required
def dashboard(request):
    return render(request, "finance/dashboard.html")


@login_required
def visualization(request):
    return render(request, 'finance/visualization.html')

@login_required
def homepage(request):
    return render(request, 'finance/homepage.html')

@login_required
def transaction_container(request):
    transactions = Transaction.objects.filter(user=request.user)

    # Filtering
    filter_form = TransactionFilterForm(request.GET or None)
    if filter_form.is_valid():
        if filter_form.cleaned_data['transaction_type']:
            transactions = transactions.filter(type=filter_form.cleaned_data['transaction_type'])
        if filter_form.cleaned_data['start_date']:
            transactions = transactions.filter(date__gte=filter_form.cleaned_data['start_date'])
        if filter_form.cleaned_data['end_date']:
            transactions = transactions.filter(date__lte=filter_form.cleaned_data['end_date'])
        if filter_form.cleaned_data['category']:
            transactions = transactions.filter(category__icontains=filter_form.cleaned_data['category'])

    # Aggregates
    total_income = transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    net_income = total_income - total_expenses

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'filter_form': filter_form
    }
    return render(request, 'finance/transaction_container.html', context)

