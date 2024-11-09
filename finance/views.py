from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.db import models
from django.http import JsonResponse

@login_required
def advice(request):
    return render(request, "finance/advice.html")


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

        # Handle adding a transaction
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    # Fetch transactions for the dashboard
    transactions = Transaction.objects.all()
    total_income = transactions.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = transactions.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
    net_income = total_income - total_expenses

    # Calculate total amount per category
    category_totals = transactions.filter(type='expense').values('category').annotate(total=Sum('amount'))

    # Define categories for labels (ensure it matches the frontend)
    categories = ['Transport', 'Salary', 'Food', 'Bills', 'Medical', 'Housing', 'Clothes']

    # Create a dictionary for quick lookup of category totals
    category_totals_dict = {item['category']: item['total'] for item in category_totals}

    # Map the category totals into the correct order for the frontend chart
    category_data = [category_totals_dict.get(cat, 0) for cat in categories]

    # Prepare context for the template
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'form': TransactionForm(),  # Form for adding transactions
        'category_data': category_data,  # Data for the category pie chart
    }

    return render(request, 'finance/dashboard.html', context)


def visualization(request):
    # Fetch total income and expenses
    total_income = Transaction.objects.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = Transaction.objects.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

    # Fetch total amount per category for pie chart
    category_totals = Transaction.objects.filter(type='expense').values('category').annotate(total=Sum('amount'))

    # Define categories for labels (ensure it matches the frontend)
    categories = ['Transport', 'Salary', 'Food', 'Bills', 'Medical', 'Housing', 'Clothes']

    # Create a dictionary for quick lookup of category totals
    category_totals_dict = {item['category']: item['total'] for item in category_totals}

    # Map the category totals into the correct order for the frontend chart
    category_data = [category_totals_dict.get(cat, 0) for cat in categories]

    # Return data as JSON
    data = {
        'totalIncome': total_income,
        'totalExpenses': total_expenses,
        'categoryData': category_data
    }
    return JsonResponse(data)