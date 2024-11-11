// Mock data - Replace this with data fetched from your backend
const incomeData = { labels: ["Salary", "Investments", "Misc"], data: [10000, 7000, 3000] };
const expenseData = { labels: ["Rent", "Groceries", "Travel"], data: [4000, 2000, 1000] };
const incomeTotal = 20000; // Total income amount
const expenseTotal = 15000; // Total expenses amount

// Bar Chart for Income vs Expenses
const barCtx = document.getElementById('barChart').getContext('2d');
const barChart = new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: ["Income", "Expenses"],
        datasets: [{
            label: 'Amount',
            data: [incomeTotal, expenseTotal],
            backgroundColor: ['#4e73df', '#e74a3b']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Total Income vs Expenses' }
        }
    }
});

// Pie Chart for Income Categories
const incomePieCtx = document.getElementById('incomePieChart').getContext('2d');
const incomePieChart = new Chart(incomePieCtx, {
    type: 'pie',
    data: {
        labels: incomeData.labels,
        datasets: [{
            data: incomeData.data,
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'right' },
            title: { display: true, text: 'Total Amount per Category (Income)' }
        }
    }
});

// Pie Chart for Expense Categories
const expensePieCtx = document.getElementById('expensePieChart').getContext('2d');
const expensePieChart = new Chart(expensePieCtx, {
    type: 'pie',
    data: {
        labels: expenseData.labels,
        datasets: [{
            data: expenseData.data,
            backgroundColor: ['#e74a3b', '#f6c23e', '#858796']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'right' },
            title: { display: true, text: 'Total Amount per Category (Expenses)' }
        }
    }
});

// Filter Function (you can adjust this function based on your backend data structure)
function applyFilters() {
    const formData = new FormData(document.getElementById('filterForm'));
    const selectedCategories = formData.getAll('category');
    const type = formData.get('type');
    const startDate = formData.get('startDate');
    const endDate = formData.get('endDate');

    // Process filters (send filters to backend, fetch data, and update charts accordingly)
    // Example: fetch('/api/transactions', { method: 'POST', body: formData })
    // .then(response => response.json())
    // .then(data => {
    //     Update chart data here based on the filtered results
    // });
}
