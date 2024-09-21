let totalIncome = 0;
        let totalExpenses = 0;
        let budget = 0;
        let savingsGoal = 0;
        let amountSaved = 0;

        function addTransaction() {
            const transactionType = document.getElementById('transactionType').value;
            const transactionAmount = parseFloat(document.getElementById('transactionAmount').value);

            if (transactionType === 'income') {
                totalIncome += transactionAmount;
            } else {
                totalExpenses += transactionAmount;
            }
            updateSummary();
        }

        function setBudget() {
            budget = parseFloat(document.getElementById('budgetAmount').value);
            updateSummary();
        }

        function trackSavings() {
            savingsGoal = parseFloat(document.getElementById('savingsGoal').value);
            amountSaved = parseFloat(document.getElementById('savingsAmount').value);
            updateSummary();
        }

        function updateSummary() {
            const balance = totalIncome - totalExpenses;

            document.getElementById('summaryBudget').innerText = `Budget: $${budget}`;
            document.getElementById('summarySavings').innerText = `Savings Goal: $${savingsGoal}`;
            document.getElementById('summaryIncome').innerText = `Total Income: $${totalIncome}`;
            document.getElementById('summaryExpenses').innerText = `Total Expenses: $${totalExpenses}`;
            document.getElementById('summaryBalance').innerText = `Remaining Balance: $${balance}`;
        }