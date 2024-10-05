const transactionList = document.getElementById('transaction-list');
const totalIncomeElement = document.getElementById('total-income');
const totalExpensesElement = document.getElementById('total-expenses');
const netIncomeElement = document.getElementById('net-income');

let transactions = JSON.parse(localStorage.getItem('transactions')) || [];

function updateTotals() {
    const totalIncome = transactions
        .filter(t => t.type === 'income')
        .reduce((acc, t) => acc + parseFloat(t.amount), 0);
    const totalExpenses = transactions
        .filter(t => t.type === 'expense')
        .reduce((acc, t) => acc + parseFloat(t.amount), 0);
    const netIncome = totalIncome - totalExpenses;

    totalIncomeElement.textContent = `$${totalIncome.toFixed(2)}`;
    totalExpensesElement.textContent = `$${totalExpenses.toFixed(2)}`;
    netIncomeElement.textContent = `$${netIncome.toFixed(2)}`;
}

function addTransactionToDOM(transaction, index) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td>${transaction.date}</td>
        <td>${transaction.category}</td>
        <td>${transaction.type}</td>
        <td>$${parseFloat(transaction.amount).toFixed(2)}</td>
        <td>
            <button class="delete-btn" onclick="deleteTransaction(${index})">Delete</button>
        </td>
    `;
    transactionList.appendChild(tr);
}

function updateTransactionList() {
    transactionList.innerHTML = '';
    transactions.forEach((transaction, index) => {
        addTransactionToDOM(transaction, index);
    });
    updateTotals();
}

function deleteTransaction(index) {
    transactions.splice(index, 1);
    localStorage.setItem('transactions', JSON.stringify(transactions));
    updateTransactionList();
}

document.getElementById('add-transaction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const date = document.getElementById('date').value;
    const category = document.getElementById('category').value;
    const type = document.getElementById('type').value;
    const amount = document.getElementById('amount').value;

    const transaction = { date, category, type, amount };
    transactions.push(transaction);

    localStorage.setItem('transactions', JSON.stringify(transactions));
    updateTransactionList();

    // Clear the form
    document.getElementById('add-transaction-form').reset();
});

// Load initial transactions from localStorage
updateTransactionList();
