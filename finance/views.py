from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.db import models

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
def dashboard(request):
    # Handle transaction deletion
    if request.method == 'POST':
        if 'delete_transaction_id' in request.POST:
            transaction_id = request.POST.get('delete_transaction_id')
            transaction = get_object_or_404(Transaction, id=transaction_id)
            transaction.delete()
            return redirect('dashboard')

        # Handle adding a transaction (this part should already be there)
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    # Calculate totals for the dashboard
    transactions = Transaction.objects.all()
    total_income = transactions.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = transactions.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
    net_income = total_income - total_expenses

    # Render the dashboard with context
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'form': TransactionForm(),  # Form for adding transactions
    }

    return render(request, 'finance/dashboard.html', context)
