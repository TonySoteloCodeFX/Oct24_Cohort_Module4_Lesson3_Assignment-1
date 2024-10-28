import classes

# =====================================================

food_budget = classes.BudgetCategory("Food", 100)
entertainment_budget = classes.BudgetCategory("Entertainment", 200)

food_budget.add_expense('Pizza', 28.75)
food_budget.add_expense('Sodas', 18.75)
food_budget.add_expense('Beer', 30.45)

entertainment_budget.add_expense('Movies', 15.00)
entertainment_budget.add_expense('Concert', 45.00)

food_budget.set_category_name('Groceries')
food_budget.set_category_budget(200)

food_budget.display_expenses()

classes.BudgetCategory.display_categories()