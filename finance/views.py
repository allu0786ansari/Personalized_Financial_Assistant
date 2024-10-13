from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
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

def homepage(request):
    transactions = Transaction.objects.all()
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    net_income = total_income - total_expenses

    return render(request, 'homepage.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
    })

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print(form.errors)  # Print errors to console
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    transaction.delete()
    return redirect('dashboard')